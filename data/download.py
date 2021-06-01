from dataclasses import dataclass
from functools import lru_cache
from typing import Optional

from translator.translator import _


@dataclass
class SoftwareCategory:
    name: str
    friendly_name: str
    icon: str
    description: Optional[str] = None


categories = (
    SoftwareCategory(
        name="documentation",
        friendly_name=_("Документация"),
        icon="doc.png",
        description=_(
            "Руководства пользователя, паспорт продукта и другая "
            "техническая документация."
        ),
    ),
    SoftwareCategory(
        name="datasheet",
        friendly_name=_("Брошюры"),
        icon="brochure.png",
        description=_("Информация о продукте."),
    ),
    SoftwareCategory(
        name="driver",
        friendly_name=_("Драйвер"),
        icon="driver.png",
        description=_("Драйвера для ОС Windows (для ОС Linux драйвер не нужен)."),
    ),
    SoftwareCategory(
        name="firmware",
        friendly_name=_("Прошивка"),
        icon="firmware.png",
        description=_(
            "Обновление прошивки осуществляется с помощью кроссплатформенного "
            "ПО EPCBoot (ссылка на скачивание на этой странице)."
        ),
    ),
    SoftwareCategory(
        name="software",
        friendly_name=_("Программное обеспечение"),
        icon="software.png",
        description=_(
            "Пользовательское программное обеспечение для поиска неисправностей "
            "на печатных платах с использованием аналоговых сигнатурных "
            "анализаторов EyePoint. Для работы ПО требуется Python 3.6.8 (win32) "
            "с набором необходимых библиотек, драйвер, а также Распространяемые "
            "пакеты Microsoft Visual C++ для Visual Studio 2013 (win32). Всё это "
            "можно скачать на данной странице."
        ),
    ),
    SoftwareCategory(
        name="debugger",
        friendly_name=_("uRPC Debugger"),
        icon="software.png",
        description=_(
            "Кроссплатформенное ПО с графическим интерфейсом для отладки "
            "сигнатурных анализаторов EyePoint IVM. Данное ПО позволяет "
            "вручную вызывать команды управления. Формирование и разбор "
            "полей сложных команд осуществляется автоматически. ПО "
            "распространяется в виде бинарных файлов, и в виде исходных "
            "кодов. Для работы на Windows требуется драйвер."
        ),
    ),
    SoftwareCategory(
        name="epcboot",
        friendly_name=_("EPCBoot"),
        icon="software.png",
        description=_(
            "Кроссплатформенное ПО для обновления прошивок сигнатурных анализаторов "
            "EyePoint и его исходные коды. "
            "Репозиторий EPCBoot на GitHub: <a href='https://github.com/EPC-MSU/"
            "EPCboot'>https://github.com/EPC-MSU/EPCboot</a>"
        ),
    ),
    SoftwareCategory(
        name="image",
        friendly_name=_("Прошивка встроенного компьютера"),
        icon="software.png",
        description=_(
            "Образы встроенной операционной системы для устройств серии EyePoint S. "
            "Обновление образа осуществляется посредством записи на SD карту. "
            "Более подробная информация содержится в руководстве пользователя. "
            "Для записи образа на SD карту в ОС Windows можно использовать "
            "Win32 Disk Imager (можно скачать с официального сайта или с данной "
            "страницы)."
        ),
    ),
    SoftwareCategory(
        name="library_doc",
        friendly_name=_("Описание библиотеки для программного управления"),
        icon="software.png",
        description=_(
            "Документация к библиотеке libivm, которая может быть использована для "
            "взаимодействия с измерителями ВАХ EyePoint IVM. Саму библиотеку можно "
            "скачать на этой странице."
        ),
    ),
    SoftwareCategory(
        name="supporting_software",
        friendly_name=_("Стороннее вспомогательное ПО"),
        icon="software.png",
        description=_(
            "Дополнительное стороннее программное обеспечение, "
            "которое может потребоваться при работе с устройствами EyePoint."
        ),
    ),
    SoftwareCategory(
        name="library",
        friendly_name=_("Библиотека для программного управления"),
        icon="software.png",
        description=_(
            "Кроссплатформенная библиотека для работы с измерителями ВАХ EyePoint "
            "IVM (измеритель сигнатур, который используется в различных "
            "устройствах линейки EyePoint). Библиотека написана на языке C, "
            "распространяется в виде бинарных файлов (win32, win64, debian) и в "
            "виде исходных кодов. Документацию к библиотеке можно скачать отдельно "
            "на этой странице."
        ),
    ),
    SoftwareCategory(
        name="examples_and_bindings",
        friendly_name=_("Примеры использования API и биндинги " "для Python и C#"),
        icon="software.png",
        description=_(
            "Комплект примеров программного кода на языках C, C# и Python, "
            "реализующего простые измерения сигнатур с использованием EyePoint IVM "
            "(измеритель сигнатур, который используется в различных устройствах "
            "линейки EyePoint). Также в данном архиве можно найти биндинги для "
            "языков Python и C#."
        ),
    ),
)


all_software = SoftwareCategory(
    name="all",
    friendly_name=_("Полный комплект программного обеспечения"),
    icon="software.png",
    description=_("Архив со всем софтом и документацией для этого продукта"),
)


@lru_cache(maxsize=128)
def software_category_by_name(name: str) -> SoftwareCategory:
    for category in categories:
        if category.name == name:
            return category
    return SoftwareCategory(name=name, friendly_name=name, icon="software.png")


version = _("Версия")
release_date = _("Дата выпуска")
size = _("Размер")
link = _("Ссылка")
download = _("Скачать")
