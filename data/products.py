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
        name="USB_ADC",
        friendly_name=_("USBADC10 v1.0.0"),
        picture="1.jpg",
        description=_(
            " Аналого-цифровой преобразователь"
        ),
        extended_description=_("<b>USBADC10</b> - устройство, преобразующее входной аналоговый сигнал в дискретный "
                               "код, включает в себя 10 каналов 12-битного АЦП, выведенных на разъём, микроконтроллер "
                               "STM32 и USB-интерфейс, по которому подаётся питание и осуществляется считывание "
                               "оцифрованных данных. Частота преобразования USBADC10 - до 4000 отсчтетов в секунду, "
                               "одновеременно по всем каналам. В комплекте с устройством поставляется программное "
                               "обеспечение для получения измерений. ПО поддерживается ОС Windows и Linux."),
        hilights=[
            _("10 каналов"),
            _("кроссплатфор-"
              "менный GUI"),
            _("USB Type-C"),
        ],
        technical=[
            _("Диапазон входного напряжения - 0...3,3 В"),
            _("Разрешение - 0,8 мВ"),
            _("Разрядность АЦП - 12-bit"),
            _("Поддержка ОС: Windows 7/8/10 (х64/х86), Linux"),
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
