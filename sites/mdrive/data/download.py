from site_engine.specification.software import SoftwareCategory
from site_engine.translator.translator import _


categories = (
    SoftwareCategory(
        name="mdrive_direct_control",
        friendly_name=_("mDrive Direct Control"),
        icon="browse_activity.svg",
        description=_(
            "Главная программа, предназначенная для управления позиционерами, диагностики моторов, настройки двигателей и др. "
            "Информация по установке размещена в руководстве пользователя в главе <em>'5.6 Установка mDrive Direct Control'</em>. "
            "Поддерживаются Windows/Linux/macOS. Для работы на Windows скачайте файл с суффиксом <em>'win32_win64'</em>. "
            "Для работы на Macintosh скачайте файл с суффиксом <em>'osx64'</em>. Пользователям Linux подойдёт standalone версия "
            "с суффиксом <em>'x86_64.AppImage'</em>. Для старых 32-битных Linux нужен суффикс <em>'ia32.AppImage'</em>."
        ),
    ),
    SoftwareCategory(
        name="documentation",
        friendly_name=_("Руководство пользователя"),
        icon="description.svg",
        description=_(
            "Техническое описание устройства, руководство по программе mDrive Direct Control, программирование и др."
        ),
    ),
    SoftwareCategory(
        name="libximc",
        friendly_name=_("Комплект разработчика"),
        icon="gear_two.svg",
        description=_(
            "С описанием комплекта разработчика можно ознакомиться в папке <em>ximc/doc-ru/html/index.html</em> "
            "указанного ниже архива. PDF-версия руководства по программированию может быть скачана также отсюда. "
            "Примеры находятся в папке <em>examples</em>."
            "<h4>Ищете версию для arm64?</h4>"
            "Официально архитектура arm64 пока не поддерживается. Но мы уже работаем над её поддержкой. "
            "Для архитектуры arm64 доступна рабочая сборка (только для Linux). Архив <em>libximc-2.14.17-arm64.zip</em> "
            "можно найти ниже в блоке <em>Комплект разработчика</em> > <em>Старые версии</em>."
        ),
    ),
    SoftwareCategory(
        name="mdrive",
        friendly_name=_("Прошивка контроллера"),
        icon="memory.svg",
        description=_(
            "Информация по обновлению прошивки содержится в руководстве пользователя, в главе 5.3.13"
        ),
    ),
    SoftwareCategory(
        name="labview",
        friendly_name=_("Примеры для LabView (Windows)"),
        icon="code_blocks.svg",
        description=_(
            "Примеры использования контроллера в среде LabView (для Windows)"
        ),
    ),
    SoftwareCategory(
        name="inf",
        friendly_name=_("Драйвера"),
        icon="gear_two.svg",
        description=_("Драйвер для ОС Windows (для Linux и macOS драйвер не нужен). "
                      "Драйвер устанавливается автоматически при установке программного обеспечения "
                      "mDrive Direct Control. Также указанный файл можно скачать ниже."),
    ),
    SoftwareCategory(
        name="revealer",
        friendly_name=_("Revealer"),
        icon="browse_activity.svg",
        description=_(
            "Утилита для автоматического обнаружения устройств mDrive, подключенных к вашей локальной сети. "
            "Поддерживаются 64-битные версии Windows/Linux/мacOS. Версия для Linux проверена на Ubuntu, "
            "но будет работать и во многих других популярных дистрибутивах."
        ),
    ),
    SoftwareCategory(
        name="3D_models",
        friendly_name=_("3D модель"),
        icon="browse_activity.svg",
        description=_(
            "Здесь вы можете скачать актуальные 3D-модели контроллеров для проектирования и визуализации. "
            "Модели предоставлены в распространённых форматах .step"
        ),
    )
)


all_software = SoftwareCategory(
    name="all",
    friendly_name=_("Комплект последних версий программного обеспечения"),
    icon="_",
    description=_("и документации для этого продукта"),
)
