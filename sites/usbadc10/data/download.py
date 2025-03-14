from site_engine.specification.software import SoftwareCategory
from site_engine.translator.translator import _

categories = (
    SoftwareCategory(
        name="driver",
        friendly_name=_("Драйвер"),
        icon="gear_two.svg",
        description=_("Драйвер для ОС Windows (для ОС Linux драйвер не нужен)."),
    ),
    SoftwareCategory(
        name="software",
        friendly_name=_("Программное обеспечение"),
        icon="browse_activity.svg",
        description=_(
            "Пользовательское программное обеспечение для получения зависимостей "
            "напряжения от времени с помощью многоканального АЦП usbadc10. "
            "Для работы ПО потребуется драйвер. Его можно скачать на данной странице вместе с программой."
        ),
    ),
    SoftwareCategory(
        name="debugger",
        friendly_name=_("uRPC Debugger"),
        icon="browse_activity.svg",
        description=_(
            "Кроссплатформенное ПО uRPC Debugger с графическим интерфейсом для отладки usbadc10. Позволяет вручную отправлять команды управления. " "Формирование и разбор сложных команд выполняется автоматически. ПО распространяется в виде бинарных файлов, и в виде исходных кодов. " 
            "Для работы ПО на Windows требуется установить драйвер."
        ),
    ),
        SoftwareCategory(
        name="library",
        friendly_name=_("Библиотека для программного управления"),
        icon="library.svg",
        description=_(
            "Кроссплатформенная библиотека для работы с многоканальным usbadc10. "
            "Библиотека написана на языке C, "
            "распространяется в виде бинарных файлов (win64 и debian) и в "
            "виде исходных кодов. Документацию к библиотеке можно скачать отдельно "
            "на этой странице."
        ),
    ),
    SoftwareCategory(
        name="library_doc",
        friendly_name=_("Описание библиотеки для программного управления"),
        icon="description.svg",
        description=_(
            "Документация к библиотеке usbadc10, которая может быть использована для "
            "взаимодействия с устройством. Саму библиотеку можно "
            "скачать на этой странице."
        ),
    ),
    SoftwareCategory(
        name="firmware",
        friendly_name=_("Прошивка"),
        icon="memory.svg",
        description=_(
            "Обновление прошивки осуществляется с помощью кроссплатформенного "
            "ПО EPCBootGUI (ссылка на скачивание на этой странице)."
        ),
    ),
    SoftwareCategory(
        name="epcboot",
        friendly_name=_("EPCBoot GUI"),
        icon="display_settings.svg",
        description=_(
            "Удобное кроссплатформенное ПО EPCBootGUI для обновления прошивок в устройствах usbadc10."
        ),
    ),
    SoftwareCategory(
        name="examples_and_bindings",
        friendly_name=_("Примеры использования API и биндинги " "для Python и C#"),
        icon="code_blocks.svg",
        description=_(
            "Комплект примеров программного кода на языках C и Python, "
            "реализующего простые считывания оцифрованных данных с устройства usbadc10. "
            "Также в данном архиве можно найти биндинги для "
            "языков Python и C#."
        ),
    ),
    SoftwareCategory(
        name="documentation",
        friendly_name=_("Документация"),
        icon="description.svg",
        description=_(
            "Руководства пользователя, паспорт продукта и другая "
            "техническая документация."
        ),
    ),
    SoftwareCategory(
        name="datasheet",
        friendly_name=_("Брошюры"),
        icon="description.svg",
        description=_("Информация о продукте."),
    ),
    SoftwareCategory(
        name="image",
        friendly_name=_("Прошивка встроенного компьютера"),
        icon="deployed_code.svg",
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
        name="supporting_software",
        friendly_name=_("Стороннее вспомогательное ПО"),
        icon="widgets.svg",
        description=_(
            "Дополнительное стороннее программное обеспечение, "
            "которое может потребоваться при работе с устройствами usbadc10."
        ),
    ),
)


all_software = SoftwareCategory(
    name="all",
    friendly_name=_("Комплект последних версий программного обеспечения"),
    icon="_",
    description=_("и документации для этого продукта"),
)
