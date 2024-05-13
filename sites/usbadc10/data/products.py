from site_engine.specification.product import Product
from site_engine.translator.translator import _

products = (
    Product(
        name="USB_ADC",
        friendly_name=_("usbadc10 v1.1.1"),
        picture="usbadc10.png",
        description=[
            _("Аналого-цифровой преобразователь")
        ],
        extended_description=[
            _("Аналого-цифровой преобразователь usbadc10 имеет частоту до 4000 отсчётов в секунду, "
              "одновременно по всем каналам. В комплекте с устройством поставляется программное "
              "обеспечение для получения измерений. Поддерживаются ОС Windows 7 SP1 и новее, Linux "
              "(протестировано на Ubuntu 18.04, 20.04 ")
        ],
        highlights=[
            _("10 каналов"),
            _("кроссплатфор-менный GUI"),
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
