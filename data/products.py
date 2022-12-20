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
    about_us_extended_description: str
    about_us_zap_description: str
    about_us_zap_extended_description: str
    picture: str
    technical: List[str]
    hilights: List[str]


products = (
    Product(
        name="USB_ADC",
        friendly_name=_("USBADC10 v1.0.0"),
        picture="2_1.png",
        description=_(
            " Аналого-цифровой преобразователь"
        ),
        extended_description=_(
            "Аналого-цифровой преобразователь USBADC10 имеет частоту до 4000 отсчётов в секунду, "
            "одновременно по всем каналам. В комплекте с устройством поставляется программное "
            "обеспечение для получения измерений. ПО поддерживается ОС Windows и Linux. Все необходимое "
            "<b>программное обеспечение</b> можно найти в свободном доступе. "
        ),

        about_us_extended_description=_(
            "Центр инженерной физики МГУ имени М.В. Ломоносова (сокращенно ООО ""ЦИФ МГУ имени М.В. Ломоносова"") "
            "занимается разработкой и продажей сложной электроники и интеллектуального программного обеспечения, "
            "наукоемкими проектами в сфере робототехники и управления движением, автоматизацией "
            "экспериментальных установок в лазерной физике и физике высоких энергий, созданием систем "
            "автоматического тестирования и диагностики печатных плат и электронных компонентов. "
        ),

        about_us_zap_description=_(
                                   "<b>Сергей Запуниди</b> <br>"
                                   "<b>Технический директор</b> "
        ),

        about_us_zap_extended_description=_(
            "Кандидат физико-математических наук, окончил физический факультет МГУ имени М.В. Ломоносова. "
            "Эксперт в области встраиваемых систем, алгоритмов управления движением. "
            "Автор пяти курсов для технических факультетов МГУ имени М.В. Ломоносова по программированию "
            "и электронике и около двадцати статей международного уровня. "
            "Руководитель и участник многочисленных научных программ и разработок. Основанная специализация "
            "в компании: руководство производственным подразделением, выработка технических решений и "
            "внедрение  новых технологий. "
        ),

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
