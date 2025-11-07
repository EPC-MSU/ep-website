from site_engine.specification.software import SoftwareCategory
from site_engine.translator.translator import _


categories = (
    SoftwareCategory(
        name="documentation",
        friendly_name=_("Документация"),
        icon="description.svg",
        description=_(
            "Инструкция по эксплуатации, паспорт продукта и другая "
            "техническая документация."
        ),
    ),
    SoftwareCategory(
        name="Promo",
        friendly_name=_("Промо"),
        icon="description.svg",
        description=_("Информация о продукте."),
    ),
    SoftwareCategory(
        name="driver",
        friendly_name=_("Драйвер"),
        icon="gear_two.svg",
        description=_("Драйвера для ОС Windows (для ОС Linux драйвер не нужен)."),
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
        name="EPLab_software",
        friendly_name=_("Программное обеспечение EPLab"),
        icon="browse_activity.svg",
        description=_(
            "Основное ПО для работы с приборами EyePoint, подключенными к компьютеру. "
            "Для работы ПО на Windows потребуется установить драйвер, а также распространяемые пакеты Microsoft Visual C++ "
            "для Visual Studio версий 2013 и 2015 годов (обязательно обе версии, пакеты не кумулятивные!). Всё это можно скачать на данной странице. <br />"
            "Версии для Windows имеют суффикс win32 или win64 (32-битная или более современная 64-битная версия). "
            "Версия для Linux имеет суффикс debian, но заработает почти на любом Linux."
        ),
    ),
    SoftwareCategory(
        name="EyePointS_software",
        friendly_name=_("Программное обеспечение EyePoint S"),
        icon="browse_activity.svg",
        description=_(
            "Графический интерфейс, аналогичный встроенному в EyePoint S*. Он может пригодиться, если хочется "
            "использовать привычный интерфейс линейки S, но на большом экране. Однако при работе с компьютера рекомендуется "
            "использовать ПО EPLab. <br />"
            "Для работы ПО нужно будет подключить EyePoint S* по USB к компьютеру, поставить драйвер, а также распространяемые пакеты Microsoft Visual C++ "
            "для Visual Studio версий 2013 и 2015 годов (обязательно обе версии, пакеты не кумулятивные!). Всё это можно скачать на данной странице."
        ),
    ),
    SoftwareCategory(
        name="debugger",
        friendly_name=_("uRPC Debugger"),
        icon="browse_activity.svg",
        description=_(
            "Кроссплатформенное ПО с графическим интерфейсом для отладки устройств EyePoint. Данное ПО предназначено для программистов, "
            "которые пишут свои программы управления для модулей и устройств EyePoint. Оно позволяет вручную вызывать команды управления, " "задавать их параметры и получать информацию от устройства. Формирование и разбор полей сложных команд осуществляется "
            "автоматически. ПО распространяется в виде бинарных файлов и в виде исходных кодов. Для работы на Windows требуется "
            "установить драйвер."
        ),
    ),
    SoftwareCategory(
        name="epcboot",
        friendly_name=_("EPCBootGUI"),
        icon="display_settings.svg",
        description=_(
            "Кроссплатформенное ПО для обновления прошивок в устройствах EyePoint. Рекомендуется использовать версию с графическим "
            "интерфейсом epcboot_gui. <br />"
            "Версии для Windows имеют суффикс win32 или win64 (32-битная или более современная 64-битная версия). "
            "Версия для Linux имеет суффикс debian, но заработает почти на любом Linux."
        ),
    ),
    SoftwareCategory(
        name="image",
        friendly_name=_("Прошивка встроенного компьютера"),
        icon="deployed_code.svg",
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
        icon="description.svg",
        description=_(
            "Документация к библиотеке, которая может быть использована для "
            "взаимодействия с устройствами EyePoint. Саму библиотеку можно скачать на этой странице."
        ),
    ),
    SoftwareCategory(
        name="supporting_software",
        friendly_name=_("Стороннее вспомогательное ПО"),
        icon="widgets.svg",
        description=_(
            "Дополнительное стороннее программное обеспечение, которое обычно уже установлено на компьютер. Однако для новых "
            "компьютеров и в других редких случаях его может быть необходимо установить для работы с устройствами EyePoint."
        ),
    ),
    SoftwareCategory(
        name="library",
        friendly_name=_("Библиотека для программного управления"),
        icon="library.svg",
        description=_(
            "Кроссплатформенная библиотека для работы с устройствами линейки EyePoint. "
            "Библиотека написана на языке C, распространяется в виде бинарных файлов (win32, win64, debian) и в "
            "виде исходных кодов. <br>"
            "Документацию к библиотеке можно скачать отдельно на этой странице."
        ),
    ),
    SoftwareCategory(
        name="examples_and_bindings",
        friendly_name=_("Примеры использования API и биндинги для Python и C#"),
        icon="code_blocks.svg",
        description=_(
            "Комплект примеров программного кода на языках Python, C и C# для устройств линейки EyePoint. "
            "Свежую версию библиотеки для Python можно установить через пакетный менеджер pip: "
            "<code>pip install ivm</code> (<a href='https://pypi.org/project/ivm/'>страница библиотеки на PyPi</a>). <br>"
            "Также в приложенных архивах можно найти биндинги для языков Python, C и C#."
        ),
    ),
    SoftwareCategory(
        name="3D_models",
        friendly_name=_("3D модель"),
        icon="browse_activity.svg",
        description=_(
            "Здесь вы можете скачать актуальные 3D-модели контроллеров для проектирования и визуализации. "
            "Модели предоставлены в распространенном .step формате"
        ),
    ),
    SoftwareCategory(
        name="server",
        friendly_name=_("Сервер"),
        icon="dns.svg",
        description=_(
            "Локальный сервер для работы с устройством EyePoint H10. "
        ),
    ),
)


all_software = SoftwareCategory(
    name="all",
    friendly_name=_("Комплект последних версий программного обеспечения"),
    icon="_",
    description=_("и документации для этого продукта"),
)
