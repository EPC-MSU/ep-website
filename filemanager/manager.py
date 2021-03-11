import asyncio
import logging
import urllib.parse as urllib
import zipfile
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from datetime import date
from os.path import getmtime, sep, join as join_path, basename, isfile
from os import remove, listdir
from typing import Dict, List, Optional

from filemanager.walker.walk import FileInfo, walk


@dataclass()
class ArchiveInfo:
    date: date
    link: str

    @classmethod
    def fromfile(cls, path: str, url_prefix: str) -> "ArchiveInfo":
        """
        :param url_prefix: url prefix, for example: /static
        :param path: path to file
        :return: "Archive"
        """

        # convert /foo/bar/spam/download/EyePointS1/all.zip to EyePointS1/all.zip
        path_short = join_path(*path.split(sep)[-2:])

        return ArchiveInfo(
            date.fromtimestamp(getmtime(path)),
            urllib.quote(join_path(url_prefix, path_short)),
        )


def archive(software: Dict[str, List[FileInfo]], zip_path: str):
    """
    Make archive with latest releases
    :param software: software, smth like
    {
        "firmware": [
            FileInfo, FileInfo, FileInfo
        ],
        "debugger": [
            FileInfo, FileInfo
        ], etc
    }
    :param zip_path: path to output zip archive
    :return:
    """
    z_file = zipfile.ZipFile(zip_path, "w")
    for category, files in software.items():
        if not files:
            continue
        prev_file = files[0]
        z_file.write(prev_file.full_path, join_path(category, prev_file.basename))
        for file in files:
            # Files ordered by version. So, we skip all older versions  with same names and platforms
            if file.name != prev_file.name or file.platform != prev_file.platform:
                z_file.write(file.full_path, join_path(category, file.basename))
            prev_file = file


def compare_latest_software(
    old: Dict[str, List[FileInfo]], new: Dict[str, List[FileInfo]]
) -> bool:
    """
    Compare software files (equal\not equal)
    :param old: old structure
    :param new: new structure
    :return: bool (equal\not equal)
    """
    if old.keys() != new.keys():
        return False  # New software category was added

    for category in old.keys():
        # There were no files in this category and now there are no files either
        if not new[category] and not old[category]:
            continue

        # Files in this category appeared or disappeared
        if not new[category] or not old[category]:
            return False

        if new[category][0] != old[category][0]:
            return False  # Last file was updated

    return True


class FileManager:
    _archive_name_format = "{product}_Full_software_package-{date}.zip"

    @classmethod
    def _archive_name(cls, product: str) -> str:
        return cls._archive_name_format.format(product=product,
                                               date=date.today().strftime("%Y.%m.%d"))

    def __init__(self, timeout: int, directory: str, url_prefix: str):
        """
        Create file manager
        :param timeout: structure refresh timeout, seconds
        :param url_prefix: url prefix for generated files
        :param directory: directory with download files to monitor
        """
        self._timeout = timeout
        self._url_prefix = url_prefix
        self._directory = directory
        self._files = None
        self._loop = None
        self._archives: Dict[str, ArchiveInfo] = dict()

    @property
    def files(self):
        if not self._files:
            raise RuntimeError("Refresh procedure not started yet")
        return self._files

    @property
    def archives(self):
        if not self._archives:
            raise RuntimeError("Refresh procedure not started yet")
        return self._archives

    def start_refresh(self, loop: Optional[asyncio.AbstractEventLoop] = None):
        """
        Start refresh loop
        :return:
        """
        _loop = loop or asyncio.get_event_loop()
        if self._loop:
            raise RuntimeError("Already started")
        self._loop: asyncio.AbstractEventLoop = _loop
        self._loop.create_task(self._periodic_task())

    async def _refresh(self):
        """
        Update files structure
        :return:
        """
        new_files = walk(self._directory, self._url_prefix)
        old_files = self._files
        self._files = new_files
        with ProcessPoolExecutor() as executor:
            for product, software in new_files.items():
                archive_directory = join_path(self._directory, product)
                archive_path = join_path(archive_directory, self._archive_name(product))

                if (
                    not old_files
                    or not old_files.get(product)
                    or not isfile(archive_path)
                    or not compare_latest_software(
                        old_files[product], new_files[product]
                    )
                ):
                    logging.debug("Update archive " + product)
                    await self._loop.run_in_executor(executor, archive, software, archive_path)

                    # Remove other old archives
                    for file in listdir(archive_directory):
                        if file.endswith(".zip"):  # archive
                            if basename(archive_path) != file:  # old archive
                                try:
                                    remove(join_path(archive_directory, file))
                                except OSError as err:
                                    logging.error(f"Unable to remove {file} {err}")

                    self._archives[product] = ArchiveInfo.fromfile(
                        archive_path, self._url_prefix
                    )

    async def _periodic_task(self):
        while True:
            try:
                logging.debug("Refresh file list...")
                await self._refresh()
            except Exception as err:
                logging.error("Exception caught during file refresh: " + str(err))
            await asyncio.sleep(self._timeout)
