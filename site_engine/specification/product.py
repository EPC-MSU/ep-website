from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Product:
    name: str
    friendly_name: str
    description: List[str]
    extended_description: List[str]
    picture: List[str]
    technical: List[str]
    highlights: List[str]


def find_product_by_name(products: Tuple[Product], name: str) -> Product:
    for product in products:
        if product.name == name:
            return product
    raise ValueError("No such product ", name)
