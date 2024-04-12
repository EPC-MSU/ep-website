from site_engine.specification.software import SoftwareCategory
from site_engine.translator.translator import _


categories = (
    SoftwareCategory(
        name="documentation",
        friendly_name=_("Документация"),
        icon="doc.png",
        description=_(
            "Инструкция по эксплуатации, паспорт продукта и другая "
            "техническая документация."
        ),
    ),
    SoftwareCategory(
        name="Promo",
        friendly_name=_("Промо"),
        icon="brochure.png",
        description=_("Информация о продукте."),
    ),
    SoftwareCategory(
        name="driver",
        friendly_name=_("Драйвер"),
        icon="software.png",
        description=_("Драйвера для ОС Windows (для ОС Linux драйвер не нужен)."),
    ),
    SoftwareCategory(
        name="firmware",
        friendly_name=_("Прошивка"),
        icon="firmware.png",
        description=_(
            "Обновление прошивки осуществляется с помощью кроссплатформенного "
            "ПО EPCBootGUI (ссылка на скачивание на этой странице)."
        ),
    ),
    SoftwareCategory(
        name="EPLab_software",
        friendly_name=_("Программное обеспечение EPLab"),
        icon="app.png",
        description=_(
            "Пользовательское программное обеспечение для поиска неисправностей "
            "на печатных платах с использованием аналоговых сигнатурных "
            "анализаторов EyePoint. Для работы ПО требуется Python 3.6.8 "
            "с набором необходимых библиотек, драйвер, а также распространяемые "
            "пакеты Microsoft Visual C++ для Visual Studio 2013. Всё это "
            "можно скачать на данной странице."
        ),
    ),
    SoftwareCategory(
        name="EyePointS_software",
        friendly_name=_("Программное обеспечение EyePoint S"),
        icon="software.png",
        description=_(
            "Пользовательское программное обеспечение, аналогичное графическому "
            "интерфейсу на устройстве EyePoint S2, для поиска неисправностей на "
            "печатных платах с использованием аналоговых сигнатурных "
            "анализаторов EyePoint. Для работы ПО требуется Python 3.6.8 "
            "с набором необходимых библиотек, драйвер, а также распространяемые "
            "пакеты Microsoft Visual C++ для Visual Studio 2013. Всё это "
            "можно скачать на данной странице."
        ),
    ),
    SoftwareCategory(
        name="debugger",
        friendly_name=_("uRPC Debugger"),
        icon="app.png",
        description=_(
            "Кроссплатформенное ПО с графическим интерфейсом для отладки устройств EyePoint. "
            "Данное ПО позволяет вручную вызывать команды управления. Формирование и разбор полей сложных команд осуществляется автоматически. "
            "ПО распространяется в виде бинарных файлов, и в виде исходных кодов. Для работы на Windows требуется драйвер."
        ),
    ),
    SoftwareCategory(
        name="epcboot",
        friendly_name=_("EPCBootGUI"),
        icon="app.png",
        description=_(
            "Кроссплатформенное ПО для обновления прошивок в устройствах EyePoint. "
        ),
    ),
    SoftwareCategory(
        name="image",
        friendly_name=_("Прошивка встроенного компьютера"),
        icon="software.png",
        description=_(
            "Образы встроенной операционной системы для устройств серии EyePoint S2. "
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
        icon="doc.png",
        description=_(
            "Документация к библиотеке, которая может быть использована для "
            "взаимодействия с устройствами EyePoint. Саму библиотеку можно скачать на этой странице."
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
        icon="books.png",
        description=_(
            "Кроссплатформенная библиотека для работы с устройствами линейки EyePoint. "
            "Библиотека написана на языке C, распространяется в виде бинарных файлов (win32, win64, debian) и в "
            "виде исходных кодов. Документацию к библиотеке можно скачать отдельно на этой странице."
        ),
    ),
    SoftwareCategory(
        name="examples_and_bindings",
        friendly_name=_("Примеры использования API и биндинги для Python и C#"),
        icon="python.png",
        description=_(
            "Комплект примеров программного кода на языках C, C# и Python для устройствах линейки EyePoint. "
            "Также в данном архиве можно найти биндинги для языков Python и C#."
        ),
    ),
    SoftwareCategory(
        name="server",
        friendly_name=_("Сервер"),
        icon="software.png",
        description=_(
            "Локальный сервер для работы с устройством EyePoint H10. "
        ),
    ),
)


all_software = SoftwareCategory(
    name="all",
    friendly_name=_("Комплект последних версий программного обеспечения"),
    icon="software.png",
    description=_("Архив со всем свежим софтом и документацией для этого продукта"),
)
