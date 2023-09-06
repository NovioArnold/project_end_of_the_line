from dataclasses import dataclass

from location import Location



@dataclass
class Industry(Location):
    input_1: str | None = None
    stock_input_1: int | None = None
    max_store_input_1: int | None = None
    input_2: str | None = None
    stock_input_2: int | None = None
    max_store_input_2: int | None = None
    input_3: str | None = None
    in_stock_input_3: int | None = None
    max_store_input_3: int | None = None
    output_1: str | None = None
    stock_output_1: int | None = None
    max_store_output_1: int | None = None
    output_2: str | None = None
    stock_output_2: int | None = None
    max_store_output_2: int | None = None
    ratio: tuple | None = None

    #  extra inputs used for the freight depot
    input_4: str | None = None
    max_store_input_4: int | None = None
    input_5: str | None = None
    max_store_input_5: int | None = None
    input_6: str | None = None
    max_store_input_6: int | None = None
    input_7: str | None = None
    max_store_input_7: int | None = None
    input_8: str | None = None
    max_store_input_8: int | None = None
    input_9: str | None = None
    max_store_input_9: int | None = None
    input_10: str | None = None
    max_store_input_10: int | None = None
    input_11: str | None = None
    max_store_input_11: int | None = None
    input_12: str | None = None
    max_store_input_12: int | None = None
    input_13: str | None = None
    max_store_input_13: int | None = None
    input_14: str | None = None
    max_store_input_14: int | None = None
    input_15: str | None = None
    max_store_input_15: int | None = None
    input_16: str | None = None
    max_store_input_16: int | None = None
    input_17: str | None = None
    max_store_input_17: int | None = None
























