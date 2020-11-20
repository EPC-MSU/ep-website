import urllib.parse as urllib
from dataclasses import dataclass
from datetime import date, datetime
from distutils.version import LooseVersion
from os import listdir
from os.path import basename, getmtime, getsize, isdir
from os.path import join as join_path
from os.path import sep
from re import findall
from typing import Dict, List, Optional

import imohash

from translator import all_languages


@dataclass
class FileInfo:
    version: LooseVersion
    date: date
    size: int
    link: str
    basename: str
    full_path: str
    code: str
    platform: str
    name: str
    language: Optional[str] = None

    @classmethod
    def fromfile(cls, path: str, url_prefix: str) -> "FileInfo":
        """
        File name must be in format name-v.v.v-platform
        :param url_prefix: url prefix, for example: /static
        :param path: path to file (relative!)
        :return: "FileInfo"
        """
        file_name = basename(path)

        # Example: libivm-1.0.2-src.zip driver-1.0.0.zip
        format_matches = findall(
            r"(?P<name>\w+)-(?P<version>\d+\.\d+\.\d+)-?(?P<platform>.+)", file_name
        )
        if not format_matches:
            raise ValueError("File name " + file_name + " must be name-v.v.v-platform")
        name, version, platform = format_matches[0]

        file_language = None
        for language in all_languages:
            # pattern en.pdf, ru.exe, etc
            if platform.startswith(language + "."):
                file_language = language
                break

        # convert /foo/bar/spam/download/EyePointS1/firm
        # ware to download/EyePointS1/firmware
        path_short = join_path(*path.split(sep)[-3:])

        return FileInfo(
            version,
            datetime.fromtimestamp(getmtime(path)).date(),
            getsize(path),
            urllib.quote(join_path(url_prefix, path_short)),
            file_name,
            path,
            imohash.hashfile(path),
            platform,
            name,
            language=file_language,
        )


def _walk_software(path: str, url_prefix: str) -> List[FileInfo]:
    result = []
    for file in listdir(path):
        fullpath = join_path(path, file)
        if isdir(file):
            continue
        try:
            result.append(FileInfo.fromfile(fullpath, url_prefix))
        except ValueError:
            continue  # Ignore file with bad version (or other value errors?)
    return sorted(result, key=lambda f: f.version, reverse=True)


def _walk_product(path: str, url_prefix: str) -> Dict[str, List[FileInfo]]:
    result = {}
    for software in listdir(path):
        fullpath = join_path(path, software)
        if not isdir(fullpath):
            continue
        result[software] = _walk_software(fullpath, url_prefix)
    return result


def walk(path: str, url_prefix: str) -> Dict[str, Dict[str, List[FileInfo]]]:
    """
    Search files in directory
    :param path:
    :param url_prefix:
    :return:
    smth like:
    {"eyepoint-s1": {
        "firmware": [
            FileInfo, FilInfo, FileInfo
        ],
        "debugger": [
            FileInfo, FineInfo, FineInfo
        ]
      }
    }
    """

    result = {}

    for product in listdir(path):
        fullpath = join_path(path, product)
        if not isdir(fullpath):
            continue
        result[product] = _walk_product(fullpath, url_prefix)

    return result


if __name__ == "__main__":
    #  Run example
    result = walk("../../view/static/download", "/static/download")
    print(result)
