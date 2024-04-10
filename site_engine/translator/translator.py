import gettext
from typing import Callable

all_languages = ("ru", "en")


def _(x: str) -> str:  # dummy translator for .pot auto-generator
    return x


def translator(site: str, lang: str) -> Callable[[str], str]:
    if not lang:
        return _

    if lang not in all_languages:
        raise ValueError("No such language")

    _translators = {
        "ru": _,
        "en": gettext.translation("en", localedir=f"sites/{site}/locale", languages=["en"]).gettext,
    }

    return _translators[lang]
