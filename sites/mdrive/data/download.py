from site_engine.specification.software import SoftwareCategory
from site_engine.translator.translator import _


categories = (
    SoftwareCategory(
        name="mdrive_direct_control",
        friendly_name=_("mDrive Direct Control"),
        icon="browse_activity.svg",
        description=_(
            "Убедитесь, что все контроллеры отключены от компьютера. "
            "Информация по установке размещена в разделе "
            "<a href=\"https://doc.mdrive.tech/ru/mdrive/8SMCn-USB/mDrive_Direct_Control_application_Users_guide/mDrive_Direct_Control_installation.html\">Установка mDrive_Direct_Control.</a>"
        ),
    ),
    SoftwareCategory(
        name="documentation",
        friendly_name=_("Документация"),
        icon="description.svg",
        description=_(
            "Документация"
        ),
    ),
    SoftwareCategory(
        name="libximc",
        friendly_name=_("Комплект разработчика"),
        icon="gear_two.svg",
        description=_(
            "С описанием комплекта разработчика можно ознакомиться в разделе `Руководство по программированию' или в "
            "папке /docs-ru/index.html указанного выше архива. Библиотека находится в /ximc-2.14.20 "
            "Примеры находятся в /examples-2.14.20 "
            "PDF-версия руководства по программированию может быть скачана отсюда."
        ),
    ),
    SoftwareCategory(
        name="mdrive",
        friendly_name=_("Прошивка контроллера"),
        icon="memory.svg",
        description=_(
            "1. Скачайте файл с нужной версией прошивки. "
            "<br>2. Запустите mDrive_Direct_Control "
            "<br>3. Рекомендуется на всякий случай сохранить конфигурационный "
            "файл mDrive_Direct_Control перед обновлением прошивки."
            "<br>4. Откройте “Settings…” -> на вкладке “About device” нажмите "
            "кнопку “Update from file” и выберите новый файл прошивки."
            "<br>5. Не беспокойтесь, если программа mDrive_Direct_Control не отвечает. Подождите пока прошивка будет "
            "успешно обновлена. Обычно это занимает около 10-15 секунд."
            "<br>6. Если настройки изменились, то загрузите сохранённый конфигурационый файл и сохраните его в "
            "энергонезависимую память контроллера с помощью кнопки “Save settings to flash”."
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
        description=_("Драйвера контроллеру не требуются, но в среде Windows требуется inf-файл. Он устанавливается "
                      "автоматически при установке программного обеспечения mDrive_Direct_Control. Этот файл вы "
                      "можете найти в папке "
                      "`C:\\ Program Files\\mDrive_Direct_Control\\Driver` после установки программы "
                      "mDrive_Direct_Control. Также указанный файл можно скачать ниже:"),
    ),
    SoftwareCategory(
        name="revealer",
        friendly_name=_("REVEALER"),
        icon="browse_activity.svg",
        description=_(
            "«Revealer» предназначен для автоматического обнаружения устройств, подключенных к вашей локальной сети."
        ),
    )
)


all_software = SoftwareCategory(
    name="all",
    friendly_name=_("Комплект последних версий программного обеспечения"),
    icon="_",
    description=_("и документации для этого продукта"),
)
