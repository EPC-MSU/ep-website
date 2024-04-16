from site_engine.specification.software import SoftwareCategory
from site_engine.translator.translator import _


categories = (
    SoftwareCategory(
        name="mdrive_direct_control",
        friendly_name=_("mDrive Direct Control"),
        icon="browse_activity.svg",
        description=_(
            "Программа mDrive_Direct_Control"
        ),
    ),
    SoftwareCategory(
        name="libximc",
        friendly_name=_("Комплект разработчика"),
        icon="description.svg",
        description=_(
            "С описанием комплекта разработчика можно ознакомиться в разделе `Руководство по программированию' или в "
            "папке /docs-ru/index.html указанного выше архива. Библиотека находится в /ximc-2.14.20"
            "Примеры находятся в /examples-2.14.20 "
            "PDF-версия руководства по программированию может быть скачана отсюда."
        ),
    ),
    SoftwareCategory(
        name="mdrive",
        friendly_name=_("Прошивка контроллера"),
        icon="memory.svg",
        description=_(
            "Скачайте файл с нужной версией прошивки. "
            "Запустите mDrive_Direct_Control "
            "Рекомендуется на всякий случай сохранить конфигурационный файл mDrive_Direct_Control перед обновлением "
            "прошивки."
            "Откройте “Settings…” -> на вкладке “About device” нажмите кнопку “Update from file” и выберите новый "
            "файл прошивки."
            "Не беспокойтесь, если программа mDrive_Direct_Control не отвечает. Подождите пока прошивка будет успешно "
            "обновлена. Обычно это занимает около 10-15 секунд."
            "Если настройки изменились, то загрузите сохранённый конфигурационый файл и сохраните его в "
            "энергонезависимую память контроллера с помощью кнопки “Save settings to flash”."
        ),
    ),
    SoftwareCategory(
        name="examples_and_bindings",
        friendly_name=_("Примеры для LabView"),
        icon="code_blocks.svg",
        description=_(
            "Примеры использования контроллера в среде LabView (для Windows) можно скачать по ссылке: labview-2.14.17-Labview_12.0.7z"
        ),
    ),
    SoftwareCategory(
        name="driver",
        friendly_name=_("Драйвер"),
        icon="gear_two.svg",
        description=_("Драйвера для ОС Windows (для ОС Linux драйвер не нужен)."),
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
