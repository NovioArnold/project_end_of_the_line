from dataclasses import dataclass

from location import Location



@dataclass
class Industry(Location):
    input_1: str | None = None
    stock_input_1: int = 0
    max_store_input_1: int = 0
    input_2: str | None = None
    stock_input_2: int = 0
    max_store_input_2: int = 0
    input_3: str | None = None
    in_stock_input_3: int = 0
    max_store_input_3: int = 0
    output_1: str | None = None
    stock_output_1: int = 0
    max_store_output_1: int = 0
    output_2: str | None = None
    stock_output_2: int = 0
    max_store_output_2: int = 0
























