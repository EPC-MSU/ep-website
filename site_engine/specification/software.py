from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class SoftwareCategory:
    name: str
    friendly_name: str
    icon: str
    description: Optional[str] = None


def find_software_category_by_name(categories: Tuple[SoftwareCategory], name: str) -> SoftwareCategory:
    for category in categories:
        if category.name == name:
            return category
    return SoftwareCategory(name=name, friendly_name=name, icon="software.png")

