import asyncio
import logging
import time
import urllib.parse as urllib
import zipfile
from datetime import date
import glob
from os.path import getmtime, sep, join as join_path, basename
from os import remove
from typing import Dict, List, Optional
from asyncio.base_events import BaseEventLoop

from site_engine.filemanager.walker.walk import FileInfo, walk
from site_engine.filemanager.walker.products_xml import generate_products_xml


def exc_handler(self: BaseEventLoop, context: dict) -> None:
    # There are fix for false-positive error in asyncio
    if "Task exception was never retrieved" not in context.get("message"):
        BaseEventLoop.default_exception_handler(self, context)
    else:
        logging.info("Task exception was never retrieved")


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
        _loop.set_exception_handler(exc_handler)
        if self._loop:
            raise RuntimeError("Already started")
        self._loop: asyncio.AbstractEventLoop = _loop
        self._loop.create_task(self._periodic_task())

    async def _refresh(self):
        """
        Update files structure
        :return:
        """
        old_files = self._files
        new_files = walk(self._directory, self._url_prefix)
        self._files = new_files

        if new_files == old_files:  # Compare Dict[str: Dict[str: List[FileInfo]]]. FileInfo has __eq__, so it's ok.
            logging.info("Original files not changed. Not needed to update archives. If archive lost, update any file")
            return

        generate_products_xml(new_files)

        for product, software in new_files.items():
            for lang in self._languages:
                archive_directory = join_path(self._directory, product)
                archive_path = join_path(archive_directory, self._archive_name(product, lang))

                logging.info(f"Update {lang.upper()} archive for '{product}'")
                archive(software, archive_path, lang)
                self._archives[lang][product] = ArchiveInfo(archive_path, self._url_prefix)

                # Remove other old archives
                latest_archive_names = [self._archive_name(product, lang) for lang in self._languages]
                files = glob.glob(archive_directory + "/*.zip")
                files_to_remove = [file for file in files if basename(file) not in latest_archive_names]
                for file in files_to_remove:
                    try:
                        remove(file)
                    except OSError as err:
                        logging.error(f"Unable to remove {file} {err}")

    async def _periodic_task(self):
        while True:
            logging.info("Update archives...")
            t = time.time()
            await self._refresh()
            logging.info(f"Update archives completed in {time.time()-t:.3f} seconds")
            await asyncio.sleep(self._timeout)
