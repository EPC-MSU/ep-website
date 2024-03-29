from dataclasses import dataclass
from functools import lru_cache
from typing import List

from translator.translator import _


@dataclass
class Product:
    name: str
    friendly_name: str
    description: List[str]
    extended_description: List[str]
    picture: List[str]
    technical: List[str]
    hilights: List[str]


products = (
    Product(
        name="EyePoint_P10",
        friendly_name=_("EyePoint P10"),
        picture=[
            _("P10.png"),
        ],
        description=[
            _("Автоматическая система локализации неисправных электронных компонентов на печатных платах "),
        ],
        extended_description=[
            _(
                "Автоматическая система локализации неисправных электронных компонентов на печатных платах. <br />"
                "Автоматическая настольная система для поиска неисправных электронных компонентов на печатных платах методом АСА. "
                "Система сочетает в себе автоматическую оптическую систему распознавания выводов компонентов и летающий щуп "
                "для проведения электрического тестирования методом аналогового сигнатурного анализа. "
            ),
        ],
        hilights=[
            _("Прост в использовании"),
            _("Снизит нагрузку на инженера"),
            _("Не повредит плату"),
        ],
        technical=[
            _("Диапазон напряжения пробного сигнала: 1...12 В"),
            _("Диапазон частот пробного сигнала: 1 Гц – 1 кГц"),
            _("Габариты и вес: 604х543х473 мм, 50 кг"),
            _("Максимальный размер рабочей области: 280x275 мм"),
            _("Поддерживаемые типы корпусов: LQFP, SOIC, SMD, SOT, DIP и т.д"),
            _("Построение карты тестирования до 10 см²/мин"),
            _("Скорость тестирования: до 100 точек в мин"),
            _("Точность установки щупа: 30 мкм"),
            _("Время на смену платы: 30 сек"),
            _("Чувствительность по R: 2 Ом - 450 кОм"),
            _("Чувствительность по C: 300 пФ - 100 мкФ"),
            _("Чувствительность по L: от 270 мкГн"),
            _("Управляющий ПК: Intel core i5 с частотой не ниже 2.8 ГГц, 16 Гб RAM, SSD не менее 256 Гб"),
            _("Электропитание: ~220В, 300 Вт"),
        ],
    ),
    Product(
        name="EyePoint_B10",
        friendly_name=_("EyePoint B10"),
        picture=[
            _("B10.png"),
        ],
        description=[
            _(
                "Автоматическая система для обнаружения контрафактных, перемаркированных или неисправных "
                "электронных компонентов в BGA корпусах. "
            ),
        ],
        extended_description=[
            _(
                "Автоматическая система для обнаружения контрафактных, перемаркированных или неисправных электронных "
                "компонентов в BGA корпусах. <br />"
                "EyePoint B10 - настольная автоматическая система для обнаружения контрафактных, перемаркированных или "
                "неисправных электронных компонентов в BGA корпусах. EyePoint B10 сравнивает сигнатуры (уникальные "
                "вольт-амперные характеристики) каждого вывода исследуемой микросхемы с сохраненными в памяти опорными "
                "данными оригинального чипа и делает вывод не только об исправности исследуемого чипа, но и о его "
                "принадлежности к одной серии или ревизии с оригинальной микросхемой. Система EyePoint B10 использует "
                "летающий щуп и способна работать c BGA-корпусами, с любым существующим на сегодня расположением "
                "и шагом выводов без применения специальной оснастки или ручной настройки."
            ),
        ],
        hilights=[
            _("Прост в использовании"),
            _("Снизит нагрузку на инженера"),
            _("Не повредит плату"),
        ],
        technical=[
            _("Диапазон напряжения пробного сигнала: 1...12 В"),
            _("Диапазон частот пробного сигнала: 1 Гц – 1 кГц"),
            _("Габариты и вес: 604х543х473 мм, 50 кг"),
            _("Поддерживаемые типы корпусов: BGA, LGA, PGA, LCC, CSP"),
            _("Шаг и количество выводов: 1,5 - 0,4 мм, 8 - 2500 шт."),
            _("Расположение выводов: произвольное"),
            _("Скорость тестирования: до 100 точек в мин"),
            _("Время на смену образца: 10 сек"),
            _("Точность установки щупа: 30 мкм"),
            _("Управляющий ПК: Intel core i5 с частотой не ниже 2.8 ГГц, 16 Гб RAM, SSD не менее 256 Гб"),
            _("Электропитание: ~220В, 300 Вт"),
            _("Максимальный размер рабочей области: 280x275 мм"),
            _("Построение карты тестирования до 10 см²/мин"),
            _("Чувствительность по R: 2 Ом - 450 кОм"),
            _("Чувствительность по C: 300 пФ - 100 мкФ"),
            _("Чувствительность по L: от 270 мкГн"),
            
        ],
    ),
    Product(
        name="EyePoint_P10b",
        friendly_name=_("EyePoint P10b"),
        picture=[
            _("P10b.png"),
        ],
        description=[
            _(
                "Автоматическая система локализации неисправных электронных компонентов на печатных платах с "
                "опцией тестирования чипов BGA "
            ),
        ],
        extended_description=[
            _(
                "Автоматическая система локализации неисправных электронных компонентов на печатных платах с "
                "опцией тестирования чипов BGA. <br />"
                "EyePoint P10b - автоматическая настольная система для поиска неисправных электронных компонентов "
                "на печатных платах с опцией выявления контрафактных, перемаркерованных или поврежденных "
                "компонентов. Система сочетает в себе автоматическую оптическую систему распознавания "
                "выводов компонентов и летающий щуп для проведения электрического тестирования методом аналогового "
                "сигнатурного анализа. "
            ),
        ],
        hilights=[
            _("PCB и BGA"),
            _("Экономия времени на поиске до 3 раз"),
            _("Автоматическая проверка до 2500 выводов"),
        ],
        technical=[
            _("Диапазон напряжения пробного сигнала: 1...12 В"),
            _("Диапазон частот пробного сигнала: 1 Гц – 1 кГц"),
            _("Габариты и вес: 604х543х473 мм, 50 кг"),
            _("Максимальный размер рабочей области: 280x275 мм"),
            _("Построение карты тестирования до 10 см²/мин"),
            _("Скорость тестирования: до 100 точек в мин"),
            _("Точность установки щупа: 30 мкм"),
            _("Управляющий ПК: Intel core i5 с частотой не ниже 2.8 ГГц, 16 Гб RAM, SSD не менее 256 Гб"),
            _("Электропитание: ~220В, 300 Вт"),
            _("Поддерживаемые типы корпусов: LQFP, SOIC, SMD, SOT, DOP, BGA, LGA, PGA, LCC, CSP и тд."),
            _("Время на смену образца: 30 сек"),
            _("Чувствительность по R: 2 Ом - 450 кОм"),
            _("Чувствительность по C: 300 пФ - 100 мкФ"),
            _("Чувствительность по L: от 270 мкГн"),
            _("Шаг и количество выводов: 1,5 - 0,4 мм, 8 - 2500 шт."),
            _("Расположение выводов: произвольное"),
        ],
    ),
    Product(
        name="EyePoint_S2",
        friendly_name=_("EyePoint S2"),
        picture=[
            _("S2.png"),
        ],
        description=[
            _(
                "Настольный локализатор неисправных электронных компонентов на печатных платах методом аналогового "
                "сигнатурного анализа с частотой тестирующего сигнала до 100 кГц и со встроенным дисплеем. "
            ),
        ],
        extended_description=[_(
            "Настольный локализатор неисправных электронных компонентов на печатных платах методом аналогового "
            "сигнатурного анализа с частотой тестирующего сигнала до 100 кГц и со встроенным дисплеем. <br />"
            "Локализатор неисправных электронных компонентов с сенсорным экраном - устройство для ручного поиска "
            "неисправностей методом аналогового сигнатурного анализа."
            "EyePoint S2 – второе поколение настольной системы для локализации неисправных электронных компонентов "
            "на печатных платах. Система обладает большим удобным сенсорным экраном. Дополнительная педаль позволяет "
            "упростить управление системой. Простой и легкий прибор, частота зондирования до 100 кГц. У прибора "
            "имеется режим план тестирования, который позволяет заранее сохранить эталонную плату в базе и далее "
            "работать с такой же неисправной платой не имея эталона под рукой."
        ),
        ],
        hilights=[
            _("Простой и легкий прибор"),
            _("Частота зондирования до 100 кГц"),
            _("Доступен план тестирования "),
        ],
        technical=[
            _("Диапазон напряжения пробного сигнала: 1,2, 3,3, 5, 12 В"),
            _("Диапазон частот пробного сигнала: 1 Гц - 100 кГц"),
            _("Габариты и вес: 205х204х120 мм, 2,2 кг"),
            _("7-ми дюймовый цветной дисплей с функцией touchscreen"),
            _("Регулируемый порог совпадения сигнатур"),
            _("Внешняя педаль для дополнительного функционала"),
            _("Экспорт данных в формате PNG, json на внешний Flash накопитель"),
            _("Поддержка режима «План тестирования»"),
            _("Возможность подключения к ПК по USB: Windows, Linux"),
            _("Возможность программного управления: C/C++, C#, Python"),
            _("Диапазон тока: до 250 мкА, до 2.5 мА, до 25 мА"),
            _("Чувствительность по R: 1 Ом - 450 кОм"),
            _("Чувствительность по C: 50 пФ - 100 мкФ"),
            _("Чувствительность по L: от 1 мкГн"),
            _("Возможность сохранить screenshot экрана в формате .PNG"),
        ],
    ),
    Product(
        name="EyePoint_u21",
        friendly_name=_("EyePoint u21"),
        picture=[
            _("u21.png"),
        ],
        description=[
            _(
                "Одноканальный модуль локализатора неисправных электронных компонентов на печатных платах методом аналогового сигнатурного анализа с частотой тестирующего сигнала до 100 кГц "
            ),
        ],
        extended_description=[
            _(
                "Одноканальный модуль локализатора неисправных электронных компонентов на печатных платах методом аналогового сигнатурного анализа с частотой тестирующего сигнала до 100 кГц <br />"
                "Миниатюрная версия одноканального ручного локализатора неисправных электронных компонентов с прямым подключением к ПК, частотой до 100 кГц. EyePoint u21 – простой, компактный настольный прибор, с возможностью программного управления, младший в линейке EyePoint, поставляемый в виде моноблока и включающий корпус, плату управления и комплектующийся измерительным щупом и зажимом «Крокодил», кабелем USB для подключения к ПК. "
            ),
        ],
        hilights=[
            _("Частота зондирования до 100 кГц"),
            _("Миниатюрные размеры"),
            _("Доступен функционал старшей модели S2"),
        ],
        technical=[
            _("Диапазон напряжения пробного сигнала: 1.2, 3.3, 5, 12 В"),
            _("Диапазон частот пробного сигнала: 1 Гц - 100 кГц"),
            _("Габариты и вес: 100x65x27 мм, 0.4 кг"),
            _("Диапазон тока: до 250 мкА, до 2.5 мА, до 25 мА"),
            _("Регулируемый порог совпадения сигнатур"),
            _("Поддержка режима «План тестирования»"),
            _("Интерфейс связи USB 2.0"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),            
            _("Возможность программного управления: C/C++, C#, Qt, Python"),
            _("Напряжение питания: 5 В"),
            _("Чувствительность по R: 1 Ом - 450 кОм"),
            _("Чувствительность по C: 50 пФ - 100 мкФ"),
            _("Чувствительность по L: от 1 мкГн"),
        ],
    ),
    Product(
        name="EyePoint_u22",
        friendly_name=_("EyePoint u22"),
        picture=[
            _("u22.png"),
        ],
        description=[
            _(
                "Двухканальный модуль локализатора неисправных электронных компонентов на печатных платах методом аналогового сигнатурного анализа с частотой тестирующего сигнала до 100 кГц"
            ),
        ],
        extended_description=[
            _(
                "Двухканальный модуль локализатора неисправных электронных компонентов на печатных платах методом аналогового сигнатурного анализа с частотой тестирующего сигнала до 100 кГц <br />"
                "Миниатюрная версия двухканального ручного локализатора неисправных электронных компонентов с прямым подключением "
                "к ПК, частотой до 100 кГц. EyePoint u22 – простой, компактный настольный прибор, с возможностью программного " "управления, младший в линейке EyePoint, поставляемый в виде моноблока и включающий корпус, плату управления "
                "и комплектующийся измерительными щупами и зажимами «Крокодил», кабелем USB для подключения к ПК."
            ),
        ],
        hilights=[
            _("Частота зондирования до 100 кГц"),
            _("Миниатюрные размеры"),
            _("Доступен функционал старшей модели S2"),
        ],
        technical=[
            _("Диапазон напряжения пробного сигнала: 1.2, 3.3, 5, 12 В"),
            _("Диапазон частот пробного сигнала: 1 Гц - 100 кГц"),
            _("Габариты и вес: 175x90x40 мм, 0.4 кг"),
            _("Диапазон тока: до 250 мкА, до 2.5 мА, до 25 мА"),
            _("Регулируемый порог совпадения сигнатур"),
            _("Поддержка режима «План тестирования»"),
            _("Интерфейс связи USB 2.0"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),
            _("Возможность программного управления: C/C++, C#, Qt, Python"),
            _("Напряжение питания: 5 В"),
            _("Чувствительность по R: 1 Ом - 450 кОм"),
            _("Чувствительность по C: 50 пФ - 100 мкФ"),
            _("Чувствительность по L: от 1 мкГн"),
            
        ],
    ),
    Product(
        name="EyePoint_a2",
        friendly_name=_("EyePoint a2"),
        picture=[
            _("a2.png"),
        ],
        description=[
            _("Одноканальный OEM модуль (без корпуса) локализатора неисправных электронных компонентов "
            "(метод аналогового сигнатурного анализа, частота тестирующего сигнала до 100 кГц)"
            ),
        ],
        extended_description=[
            _(
                "Одноканальный OEM модуль (без корпуса) аналогового сигнатурного анализа. <br />"
                "EyePoint a2 - ОЕМ модуль, предназначенный для поиска неисправных электронных компонентов на печатных платах "
                "методом аналогового сигнатурного анализа (АСА). Устройство управляется по USB (через виртуальный COM-порт). "
                "Модуль имеет открытый API для разработки собственного программного обеспечения. "
                "В комплекте с устройством поставляется SDK (комплект разработчика), который включает в себя: "
                "библиотеку для языка программирования C, биндинги для языков Python и С#, "
                "примеры кода и документацию. Кроме того, модуль может использоваться совместно с готовым ПО "
                "для других устройств семейства EyePoint."
            ),
        ],
        hilights=[
            _("Открытый API"),
            _("Полный функционал"),
            _("Максимально доступный"),
        ],
        technical=[
            _("Диапазон напряжения пробного сигнала: 1.2, 3.3, 5, 12 В"),
            _("Диапазон частот пробного сигнала: 1 Гц – 100 кГц"),
            _("Габариты и вес: 60х40х5 мм, 0.012 кг"),
            _("Диапазон тока: от 25 мкА до 25 мА"),
            _("Интерфейс связи USB 2.0"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),
            _("Возможность программного управления: C/C++, C#, Qt, Python"),
            _("Напряжение питания: 5 В"),
            _("Чувствительность по R: 1 Ом - 450 кОм"),
            _("Чувствительность по C: 50 пФ - 100 мкФ"),
            _("Чувствительность по L: от 1 мкГн"),
        ],
    ),
    Product(
        name="EyePoint_H10",
        friendly_name=_("EyePoint H10"),
        picture=[
            _("H10.png"),
        ],
        description=[
            _(
                "Локализатор неисправных электронных компонентов на печатных платах "
                "с частотой тестирующего сигнала до 12 МГц "
                "и широким диапазоном выбора напряжения и чувствительности по току."
            ),
        ],
        extended_description=[
            _(
               "Локализатор неисправностей на печатных платах методом аналогового сигнатурного анализа с частотой "
               "тестирующего сигнала до 12 МГц и широким диапазоном выбора напряжения и чувствительности по току <br />"
                "EyePoint H10 – простой настольный прибор, с управлением по USB, поставляемый в виде моноблока и комплектующийся измерительными щупами, тестовой платой, кабелем USB и кабелем электропитания 220 В."
            ),
        ],
        hilights=[
            _("Частота тестирующего сигнала до 12 МГц"),
            _("Управление по USB"),
            _("Широкий диапазон напряжения"),
        ],
        technical=[
            _(
                "Диапазон напряжения пробного сигнала: 1, 1.5, 2, 2.5, 3, 4, "
                "4.5, 5, 6, 6.7, 7.5, 10 В"
            ),
            _(
                "Диапазон частот пробного сигнала: 1, 5, 10, 50, 100, 400 Гц. "
                "1.5, 6, 25, 100, 400 кГц. 1.5, 3, 6, 12 МГц"
            ),
            _("Габариты и вес: 137х65х110 мм, 0.7 кг"),
            _("Регулируемый порог совпадения сигнатур"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),
            _("Интерфейс подключения к ПК: USB"),
            _("Возможность программного управления: C/C++, Python"),
            _("Электропитание: ~220В"),
        ],
    ),
    Product(
        name="EyePoint_MUX_M",
        friendly_name=_("EyePoint MUX_M"),
        picture=[
            _("mux_m.png"),
        ],
        description=[
            _(
                "Материнская плата мультиплексора, необходимая для работы с модулями <b>Eyepoint MUX_S_A</b>. "
                "Позволяет подключать до 8 модулей на 64 канала каждый (в сумме до 512 каналов). "
                "Используется совместно с сигнатурными анализаторами линейки EyePoint. "
            ),
        ],
        extended_description=[
            _(
                "Материнская плата мультиплексора, необходимая для работы с модулями <b>Eyepoint MUX_S_A</b>. "
                "Позволяет подключать до 8 модулей на 64 канала каждый (в сумме до 512 каналов). "
                "Используется совместно с сигнатурными анализаторами линейки EyePoint. "
            ),
            _(
                "EyePoint MUX предназначен для коммутирования одного входного канала на "
                "любой из выходных каналов в заданной оператором последовательности. "
                "Используется совместно с сигнатурными анализаторами линейки EyePoint. "
                "При помощи EyePoint MUX можно производить быстрое тестирование краевых разъемов неисправных плат, "
                "а также проводить входной контроль микросхем при использовании специализированной оснастки для их "
                "установки. "
            ),
        ],
        hilights=[
            _("Скалирование модулей (до 8 штук, 512 каналов)"),
            _("Совместимость со всей линейкой приборов EyePoint"),
            _("Поддержка плана тестирования с генерацией отчетов"),
        ],
        technical=[
            _("Габариты и вес: 130x75x17.5 мм, 0,115 кг"),
            _("Интерфейс подключения к ПК: USB Type-C"),
            _("Возможность программного управления: C/C++, C#, Python"),
        ],
    ),
    Product(
        name="EyePoint_MUX_S_A",
        friendly_name=_("EyePoint MUX_S_A"),
        picture=[
            _("mux_sa.png"),
        ],
        description=[_(
            "Модуль мультиплексора на 64 канала. "
            "Позволяет зондировать каждый из 64 каналов по отношению к общему проводу (один к многим). "
            "Используется совместно с материнской платой <b>EyePoint MUX_M.</b> "
        ),
        ],
        extended_description=[_(
            "Модуль мультиплексора на 64 канала. "
            "Позволяет зондировать каждый из 64 каналов по отношению к общему проводу (один к многим). "
            "Используется совместно с материнской платой <b>EyePoint MUX_M.</b> "
        ), _(
            "EyePoint MUX предназначен для коммутирования одного входного канала на "
            "любой из выходных каналов в заданной оператором последовательности. "
            "Используется совместно с материнской платой <b>EyePoint MUX_M</b>. "
            "При помощи EyePoint MUX можно производить быстрое тестирование краевых разъемов неисправных плат, "
            "а также проводить входной контроль микросхем при использовании специализированной оснастки для их "
            "установки. "
        ),
        ],
        hilights=[
            _("Скалирование модулей (до 8 штук, 512 каналов)"),
            _("Совместимость со всей линейкой приборов EyePoint"),
            _("Поддержка плана тестирования с генерацией отчетов"),
        ],
        technical=[
            _("Диапазон напряжения пробного сигнала: до ~12 В"),
            _("Диапазон частот пробного сигнала: до 100 кГц"),
            _("Габариты и вес: 130x75x17.5 мм, 0,115 кг"),
            _("Максимальный ток пропускаемого сигнала: до 90 мА"),
            _("Сопротивление канала: 11 Ом"),
            _("Ёмкость канала: 100 пФ"),
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
