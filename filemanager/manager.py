from filemanager.walker.walk import walk, FileInfo
from typing import List, Dict, Optional
import zipfile
import logging
import asyncio
import urllib.parse as urllib
from os.path import join as join_path, sep, getmtime
from dataclasses import dataclass
from datetime import date


@dataclass()
class ArchiveInfo:
    date: date
    link: str

    @classmethod
    def fromfile(cls, path: str, url_prefix: str) -> "ArchiveInfo":
        """
        :param url_prefix: url prefix, for example: /static
        :param path: path to file (relative!)
        :return: "Archive"
        """

        # convert /foo/bar/spam/download/EyePointS1/all.zip to EyePointS1/all.zip
        path_short = join_path(*path.split(sep)[-2:])

        return ArchiveInfo(date.fromtimestamp(getmtime(path)),
                           urllib.quote(join_path(url_prefix, path_short)))


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
        file = files[0]  # newest version
        z_file.write(file.full_path, join_path(category, file.basename))


def compare_latest_software(old: Dict[str, List[FileInfo]], new: Dict[str, List[FileInfo]]) -> bool:
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
    _archive_name = "FullSDK.zip"

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
        self._archives = dict()

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
        self._loop = _loop
        self._loop.create_task(self._periodic_task())

    def _refresh(self):
        """
        Update files structure
        :return:
        """
        new_files = walk(self._directory, self._url_prefix)
        for product, software in new_files.items():
            if not self._files or \
               not self._files.get(product) or \
               not compare_latest_software(self._files[product], new_files[product]):
                logging.debug("Update archive " + product)
                archive_path = join_path(self._directory, product, self._archive_name)
                archive(software, archive_path)
                self._archives[product] = ArchiveInfo.fromfile(archive_path, self._url_prefix)
        self._files = new_files

    async def _periodic_task(self):
        while True:
            try:
                logging.debug("Refresh file list...")
                self._refresh()
            except Exception as err:
                logging.error("Exception caught during file refresh: " + str(err))
            await asyncio.sleep(self._timeout)
