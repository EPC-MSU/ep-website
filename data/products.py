from dataclasses import dataclass
from functools import lru_cache
from typing import List

from translator.translator import _


@dataclass
class Product:
    name: str
    friendly_name: str
    description: str
    extended_description: str
    picture: str
    technical: List[str]
    hilights: List[str]


products = (
    Product(
        name="EyePoint_P10",
        friendly_name=_("EyePoint P10"),
        picture="P10.png",
        description=_(
            "Автоматическая настольная система для поиска неисправных электронных компонентов на "
            "печатных платах методом АСА."
        ),
        extended_description=_(
            "Система сочетает в себе автоматическую оптическую систему распознавания выводов "
            "компонентов и летающий щуп для проведения электрического тестирования методом "
            "аналогового сигнатурного анализа."
        ),
        hilights=[
            _("Прост в использовании"),
            _("Снизит нагрузку на инженера"),
            _("Не повредит плату"),
        ],
        technical=[
            _("Метод тестирования: АСА"),
            _("Диапазон частот тестирующего сигнала: 1 Гц – 1 кГц"),
            _("Рабочие напряжения: 1,2, 3,3, 5, 12 В"),
            _("Максимальный размер платы: 280x275 мм"),
            _("Поддержка корпусов: LQFP, SOIC, SMD, SOT, DIP и т.д"),
            _("Построение карты тестирования до 10 см²/мин"),
            _("Скорость тестирования: 100 точек в мин"),
            _("Точность установки щупа: 30 мкм"),
            _("Время на смену платы: 30 сек"),
            _("Тестирующее напряжение до +/- 12 В"),
            _("Чувствительность по R 2 Ом - 450 кОм"),
            _("Чувствительность по C 300 пФ - 100 мкФ"),
            _("Чувствительность по L от 270 мкГн"),
            _("Габариты и вес: 604х543х473 мм, 50 кг"),
            _("Управляющий ПК: Intel i5 2.8 ГГц, 16 Гб RAM, 256 Гб SSD"),
            _("Электропитание: ~220В, 300 Вт"),
        ],
    ),
    Product(
        name="EyePoint_P10b",
        friendly_name=_("EyePoint P10b"),
        picture="P10b.png",
        description=_(
            "EyePoint P10b - автоматическая настольная система для поиска неисправных электронных "
            "компонентов на печатных платах с опцией выявления контрафактных, перемаркерованных или "
            "поврежденных компонентов в BGA корпусах."
        ),
        extended_description=_(
            "Система сочетает в себе автоматическую оптическую систему распознавания выводов "
            "компонентов и летающий щуп для проведения электрического тестирования методом "
            "аналогового сигнатурного анализа."
        ),
        hilights=[
            _("PCB и BGA"),
            _("Экономия времени на поиске до 3 раз"),
            _("Автоматическая проверка до 2500 выводов"),
        ],
        technical=[
            _("Метод тестирования: АСА"),
            _("Диапазон частот тестирующего сигнала: 1 Гц – 1 кГц"),
            _("Рабочие напряжения: 1,2, 3,3, 5, 12 В"),
            _("Максимальный размер платы: 280x275 мм"),
            _("Поддержка корпусов: LQFP, SOIC, SMD, SOT, DIP и т.д."),
            _("Поддержка тестирования корпусов типа BGA"),
            _("Построение карты тестирования до 10 см²/мин"),
            _("Шаг и количество выводов BGA микросхем: 1,5 - 0,4 мм, 8 - 2500 шт."),
            _("Расположение выводов: произвольное"),
            _("Скорость тестирования: 100 точек в мин"),
            _("Точность установки щупа: 30 мкм"),
            _("Время на смену платы: 30 сек"),
            _("Тестирующее напряжение до +/- 12 В"),
            _("Чувствительность по R 2 Ом - 450 кОм"),
            _("Чувствительность по C 300 пФ - 100 мкФ"),
            _("Чувствительность по L от 270 мкГн"),
            _("Предоставляются подложки для крепления BGA микросхем"),
            _("Габариты и вес: 604х543х473 мм, 50 кг"),
            _("Управляющий ПК: Intel i5 2.8 ГГц, 16 Гб RAM, 256 Гб SSD"),
            _("Электропитание: ~220В, 300 Вт"),
        ],
    ),
    Product(
        name="EyePoint_S2",
        friendly_name=_("EyePoint S2"),
        picture="S2.png",
        description=_(
            "Локализатор неисправных электронных компонентов с сенсорным экраном - устройство для "
            "ручного поиска неисправностей методом аналогового сигнатурного анализа."
        ),
        extended_description=_(
            "EyePoint S2 – второе поколение настольной системы для локализации неисправных "
            "электронных компонентов на печатных платах. Система обладает большим удобным "
            "сенсорным экраном. Дополнительная педаль позволяет упростить управление "
            "системой."
        ),
        hilights=[
            _("Простой и легкий прибор"),
            _("Частота зондирования до 100 кГц"),
            _("Доступен план тестирования "),
        ],
        technical=[
            _("Диапазон частот тестирующего сигнала: 1 Гц – 100 кГц"),
            _("Рабочие напряжения: 1,2, 3,3, 5, 12 В"),
            _("Диапазон тока: до 250 мкА, до 2.5 мА, до 25 мА"),
            _("Габариты и вес: 205х204х120 мм, 2,5 кг"),
            _("7-ми дюймовый цветной дисплей с функцией touchscreen"),
            _("Регулируемый порог совпадения сигнатур"),
            _("Внешняя педаль для дополнительного функционала"),
            _("Экспорт данных в формате .json на внешний Flash накопитель"),
            _("Возможность сохранить screenshot экрана в формате .PNG"),
            _("Поддержка режима «План тестирования»"),
            _("Возможность подключения к ПК по USB: Windows, Linux"),
            _("Возможность программного управления: C/C++, C#, Python"),
            _("Чувствительность по R 1 Ом - 450 кОм"),
            _("Чувствительность по C 50 пФ - 100 мкФ"),
            _("Чувствительность по L от 1 мкГн"),
        ],
    ),
    Product(
        name="EyePoint_u21",
        friendly_name=_("EyePoint u21"),
        picture="u21.jpg",
        description=_(
            "EyePoint u21 – миниатюрный одноканальный локализатор неисправных электронных компонентов на печатных платах методом ASA с частотой тестирующего сигнала до 100 кГц"
        ),
        extended_description=_(
            "EyePoint u21 – простой, компактный настольный прибор, с возможностью программного управления, младший в линейке EyePoint, поставляемый в виде моноблока и включающий корпус, плату управления и комплектующийся измерительным щупом и зажимом «Крокодил», кабелем USB для подключения к ПК."
        ),
        hilights=[
            _("Частота зондирования до 100 кГц"),
            _("Миниатюрные размеры"),
            _("Доступен функционал старшей модели S2"),
        ],
        technical=[
            _("Диапазон тока: до 250 мкА, до 2.5 мА, до 25 мА"),
            _("Частота пробного сигнала до 100кГц"),
            _("Метод тестирования: АСА"),
            _("Напряжение пробного сигнала 1.2, 3.3, 5, 12В"),
            _("Регулируемый порог совпадения сигнатур"),
            _("Поддержка режима «План тестирования»"),
            _("Интерфейс связи USB 2.0"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),
            _("Возможность программного управления: C#/C++, Qt, Python"),
            _("Напряжение питания: 5 В"),
            _("Чувствительность по R: 1 Ом - 450 кОм"),
            _("Чувствительность по C: 50 пФ - 100 мкФ"),
            _("Чувствительность по L: от 1 мкГн"),
            _("Габариты и вес: 100x65x27 мм, 0.4 кг"),
        ],
    ),
    Product(
        name="EyePoint_u22",
        friendly_name=_("EyePoint u22"),
        picture="u22.jpg",
        description=_(
            "EyePoint u22 – миниатюрный двухканальный локализатор неисправных электронных компонентов на печатных платах методом ASA с частотой тестирующего сигнала до 100 кГц"
        ),
        extended_description=_(
            "Миниатюрная версия двухканального ручного локализатора неисправных электронных компонентов с прямым подключением к " "ПК, частотой до 100 кГц "
            "EyePoint u22 – простой, компактный настольный прибор, с возможностью программного управления, младший в линейке EyePoint, поставляемый в виде моноблока и включающий корпус, плату управления и комплектующийся измерительными щупами и зажимами «Крокодил», кабелем USB для подключения к ПК."
        ),
        hilights=[
            _("Частота зондирования до 100 кГц"),
            _("Миниатюрные размеры"),
            _("Доступен функционал старшей модели S2"),
        ],
        technical=[
            _("Диапазон тока: до 250 мкА, до 2.5 мА, до 25 мА"),
            _("Частота пробного сигнала до 100кГц"),
            _("Метод тестирования: АСА"),
            _("Напряжение пробного сигнала 1.2, 3.3, 5, 12В"),
            _("Регулируемый порог совпадения сигнатур"),
            _("Поддержка режима «План тестирования»"),
            _("Интерфейс связи USB 2.0"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),
            _("Возможность программного управления: C#/C++, Qt, Python"),
            _("Напряжение питания: 5 В"),
            _("Чувствительность по R: 1 Ом - 450 кОм"),
            _("Чувствительность по C: 50 пФ - 100 мкФ"),
            _("Чувствительность по L: от 1 мкГн"),
            _("Габариты и вес: 175x90x40 мм, 0.4 кг"),
        ],
    ),
    Product(
        name="EyePoint_a2",
        friendly_name=_("EyePoint a2"),
        picture="a2.png",
        description=_(
            "Одноканальный OEM модуль (без корпуса) аналогового сигнатурного анализа."
        ),
        extended_description=_(
            "EyePoint a2 - ОЕМ модуль, предназначенный для поиска неисправных электронных "
            "компонентов на печатных платах методом аналогового сигнатурного анализа (АСА). "
            "Устройство управляется по USB (через виртуальный COM-порт). Модуль имеет "
            "открытый API для разработки собственного программного обеспечения. В комплекте "
            "с устройством поставляется SDK (комплект разработчика), который включает в "
            "себя: библиотеку для языка программирования C, биндинги для языков Python и С#, "
            "примеры кода и документацию. Поддерживаются ОС Windows и Linux. Кроме того, "
            "модуль может использоваться совместно с готовым ПО для других устройств "
            "семейства EyePoint."
        ),
        hilights=[
            _("Открытый API"),
            _("Полный функционал"),
            _("Максимально доступный"),
        ],
        technical=[
            _("Метод тестирования: АСА"),
            _("Диапазон частот тестирующего сигнала: 1 Гц – 100 кГц"),
            _("Рабочие напряжения: 1.2, 3.3, 5, 12 В"),
            _("Чувствительность по току: от 25 мкА до 25 мА"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),
            _("Интерфейс подключения к ПК: USB 2.0"),
            _("Возможность программного управления: C#/C++, Qt, Python"),
            _("Габариты и вес: 60х40х5 мм, 0.012 кг"),
            _("Напряжение питания: 5 В"),
            _("Чувствительность по R: 1 Ом - 450 кОм"),
            _("Чувствительность по C: 50 пФ - 100 мкФ"),
            _("Чувствительность по L: от 1 мкГн"),
            _("Питание от USB разъема"),
        ],
    ),
    Product(
        name="EyePoint_H10",
        friendly_name=_("EyePoint H10"),
        picture="H10.png",
        description=_(
            "Локализатор неисправностей на печатных платах методом сигнатурного анализа "
            "с частотой тестирующего сигнала до 12 МГц "
            "и широким диапазоном выбора напряжения и чувствительности по току."
        ),
        extended_description=_(
            "Локализатор неисправностей на печатных платах методом сигнатурного анализа "
            "с частотой тестирующего сигнала до 12 МГц "
            "и широким диапазоном выбора напряжения и чувствительности по току, что позволяет "
            "искать неисправности на высокочастотных платах. "
            "EyePoint H10 - простой настольный прибор, с управлением по USB, поставляемый в виде моноблока "
            "и комплектующийся измерительными щупами, тестовой платой, кабелем USB и кабелем "
            "электропитания 220В."
        ),
        hilights=[
            _("Частота тестирующего сигнала до 12 МГц"),
            _("Управление по USB"),
            _("Широкий диапазон напряжения"),
        ],
        technical=[
            _("Метод тестирования: АСА"),
            _("Диапазон частот тестирующего сигнала: 1, 5, 10, 50, 100, 400 Гц. "
            "1.5, 6, 25, 100, 400 кГц. 1.5, 3, 6, 12 МГц"),
            _("Рабочие напряжения: 1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 6, 6.7, 7.5, 10 В"),
            _("Регулируемый порог совпадения сигнатур"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),
            _("Интерфейс подключения к ПК: USB"),
            _("Возможность программного управления: C/C++, Python"),
            _("Габариты и вес: 137х65х110 мм, 0.7 кг"),
            _("Электропитание: ~220В"),
        ],
    ),
)

assert all([" " not in p.name for p in products])


@lru_cache(maxsize=128)
def product_by_name(name: str) -> Product:
    for product in products:
        if product.name == name:
            return product
    raise ValueError("No such product ", name)
