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
    highlights: List[str]


products = (
    Product(
        name="USB_ADC",
        friendly_name=_("usbadc10 v1.0.0"),
        picture=[
            _("UALab.png")
        ],
        description=[
            _("Аналого-цифровой преобразователь")
        ],
        extended_description=[_(
            "Аналого-цифровой преобразователь usbadc10 имеет частоту до 4000 отсчётов в секунду, "
            "одновременно по всем каналам. В комплекте с устройством поставляется программное "
            "обеспечение для получения измерений. ПО поддерживается ОС Windows и Linux. Все необходимое "
            "<b>программное обеспечение</b> можно найти в свободном доступе. "
        )],
        highlights=[
            _("10 каналов"),
            _("кроссплатфор-"
              "менный GUI"),
            _("USB Type-C"),
        ],
        technical=[
            _("Диапазон входного напряжения - 0 - 3.3 В"),
            _("Разрешение - 0.8 мВ"),
            _("Разрядность АЦП - 12-bit"),
            _("Поддержка ОС: Windows, Linux"),
            _("Разъем подключения - USB type C"),
            _("Скорость передачи данных - USB Full-Speed"),
            _("До 4000 выборок в секунду одновременно по всем каналам")
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
