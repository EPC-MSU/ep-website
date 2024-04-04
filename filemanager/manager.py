import asyncio
import logging
import urllib.parse as urllib
import zipfile
from concurrent.futures import ProcessPoolExecutor
from datetime import date
import glob
from os.path import getmtime, sep, join as join_path, basename, isfile
from os import remove
from typing import Dict, List, Optional

from filemanager.walker.walk import FileInfo, walk


class ArchiveInfo:
    def __init__(self, path: str, url_prefix: str):
        """
        :param url_prefix: url prefix, for example: /static
        :param path: path to file
        """
        # convert /foo/bar/spam/download/EyePointS1/all.zip to EyePointS1/all.zip
        path_short = join_path(*path.split(sep)[-2:])

        self.date = date.fromtimestamp(getmtime(path))
        self.link = urllib.quote(join_path(url_prefix, path_short))


def filter_files_inside_category(category_files: List[FileInfo], latest=True, lang=None) -> List[FileInfo]:
    """
    Filter releases.

    If latest=True return like [software_name-1.0.11-debian, software_name-1.0.11-win64]

    If latest=False return like [software_name-1.0.10-debian, software_name-1.0.10-win64]

    :param category_files: list of files inside category
    :param latest: Bool - select latest releases or old releases
    :param lang: Select files only with lang argument or if file has no lang
    :return: filtered list by latest argument condition
    """

    # Filter selected lang or if file has no lang
    files = [file for file in category_files if lang == file.language or file.language is None]

    # Find last version for every software_name, assuming files-list sorted by version decrease
    latest_versions = {}
    for software_name in set([file.name for file in files]):
        latest_versions[software_name] = [file.version for file in files if file.name == software_name][0]

    # Filter all files with same software_name and latest version
    filtered_latest = []
    filtered_old = []

    for file in files:
        # if file.name not in latest_versions.keys():
        #     continue

        if latest_versions[file.name] == file.version:
            filtered_latest.append(file)
        else:
            filtered_old.append(file)
    # Select latest-files-list or old-files-list by function argument
    return filtered_latest if latest else filtered_old


def filter_files(all_files, latest=True, lang=None) -> Dict[str, Dict[str, List[FileInfo]]]:
    # Filter files for all products
    filtered_dict = {}
    for product, product_software in all_files.items():
        filtered_software_files = {}
        for category, files in product_software.items():
            if not files:
                continue
            filtered_software_files[category] = filter_files_inside_category(files, latest=latest, lang=lang)
        filtered_dict[product] = filtered_software_files
    return filtered_dict


def archive(software: Dict[str, List[FileInfo]], zip_path: str, lang: str):
    """
    Make archive with latest releases
    """
    z_file = zipfile.ZipFile(zip_path, "w")

    for category, files in software.items():
        selected_files = filter_files_inside_category(files, latest=True, lang=lang)
        for file in selected_files:
            z_file.write(file.full_path, join_path(category, file.basename))


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
    _archive_name_format = "{product}_Full_software_package-{lang}-{date}.zip"

    @classmethod
    def _archive_name(cls, product: str, language: str) -> str:
        return cls._archive_name_format.format(product=product,
                                               lang=language,
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
        self._languages = ['ru', 'en']
        self._archives: Dict[str, Dict[str, ArchiveInfo]] = {lang: {} for lang in self._languages}

    @property
    def files(self):
        if not self._files:
            raise RuntimeError("Refresh procedure not done yet")
        return self._files

    @property
    def archives(self):
        if not self._archives:
            raise RuntimeError("Refresh procedure not done yet")
        return self._archives

    def releases(self, latest=True, lang='ru') -> Dict[str, Dict[str, List[FileInfo]]]:
        return filter_files(self.files, latest=latest, lang=lang)

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
                for lang in self._languages:
                    archive_directory = join_path(self._directory, product)
                    archive_path = join_path(archive_directory, self._archive_name(product, lang))

                    # TODO: Is this check actually work?
                    if old_files and old_files.get(product) and isfile(archive_path) and \
                            compare_latest_software(old_files[product], new_files[product]):
                        continue

                    logging.debug(f"Update {lang.upper()} archive for '{product}'")
                    await self._loop.run_in_executor(executor, archive, software, archive_path, lang)
                    self._archives[lang][product] = ArchiveInfo(archive_path, self._url_prefix)

                    # Remove other old archives
                    latest_archive_names = [self._archive_name(product, lang) for lang in self._languages]
                    files = glob.glob(archive_directory + "*.zip")
                    files_to_remove = [file for file in files if basename(file) not in latest_archive_names]

                    for file in files_to_remove:
                        try:
                            remove(join_path(archive_directory, file))
                        except OSError as err:
                            logging.error(f"Unable to remove {file} {err}")

    async def _periodic_task(self):
        while True:
            try:
                logging.debug("Refresh file list...")
                await self._refresh()
                logging.debug("Refresh file list done.")
            except Exception as err:
                logging.error("Exception caught during file refresh: " + str(err))
            await asyncio.sleep(self._timeout)
