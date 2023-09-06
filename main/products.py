from dataclasses import dataclass

@dataclass
class Product:
    product_name: str
    produced_by: str
    consumed_by: list[str]