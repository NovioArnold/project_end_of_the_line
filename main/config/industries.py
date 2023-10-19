
from enum import StrEnum
from typing import Optional

from dataclasses import dataclass, field

from main.config.products import Products


"""init products base class"""
PRODUCT = Products


class Industries(StrEnum):
    """ All the industries on the railroad"""
    logging_camp = 'logging_camp'
    sawmill = 'sawmill'
    iron_mine = 'iron_mine'
    smelter = 'smelter'
    coal_mine = 'coal_mine'
    steel_mill = 'steel_mill'
    oil_well = 'oil_well'
    oil_refinery = 'oil_refinery'
    freight_depot = 'freight_depot'


@dataclass
class IndustryConfig:
    """Industry input output config"""
    input_1: str = PRODUCT.not_in_use
    stock_input_1: int = 0
    max_store_input_1: int = 0
    input_2: str = PRODUCT.not_in_use
    stock_input_2: int = 0
    max_store_input_2: int = 0
    input_3: str = PRODUCT.not_in_use
    stock_input_3: int = 0
    max_store_input_3: int = 0
    output_1: str = PRODUCT.not_in_use
    stock_output_1: int = 0
    max_store_output_1: int = 0
    output_2: str = PRODUCT.not_in_use
    stock_output_2: int = 0
    max_store_output_2: int = 0
    output_3: str = PRODUCT.not_in_use
    stock_output_3: int = 0
    max_store_output_3: int = 0
    output_4: str = PRODUCT.not_in_use
    stock_output_4: int = 0
    max_store_output_4: int = 0
    output_5: str = PRODUCT.not_in_use
    stock_output_5: int = 0
    max_store_output_5: int = 0
    output_6: str = PRODUCT.not_in_use
    stock_output_6: int = 0
    max_store_output_6: int = 0
    output_7: str = PRODUCT.not_in_use
    stock_output_7: int = 0
    max_store_output_7: int = 0
    output_8: str = PRODUCT.not_in_use
    stock_output_8: int = 0
    max_store_output_8: int = 0
    output_9: str = PRODUCT.not_in_use
    stock_output_9: int = 0
    max_store_output_9: int = 0
    output_10: str = PRODUCT.not_in_use
    stock_output_10: int = 0
    max_store_output_10: int = 0
    output_11: str = PRODUCT.not_in_use
    stock_output_11: int = 0
    max_store_output_11: int = 0
    output_12: str = PRODUCT.not_in_use
    stock_output_12: int = 0
    max_store_output_12: int = 0
    output_13: str = PRODUCT.not_in_use
    stock_output_13: int = 0
    max_store_output_13: int = 0
    production_ratio: Optional[production_ratio] = field(default_factory=dict)


"""init industries base class"""
industries = Industries


"""init production ratio per industry"""
production_ratio: dict[industries] = {
     industries.sawmill: {
        "input": 2,
        "output": 2,
     },
     industries.smelter: {
        "input": 2,
        "output": 2,
     },
     industries.logging_camp: {
        "input": 0,
        "output": 2,
     },
     industries.oil_refinery: {
        "input": 2,
        "output": 2,
     },
     industries.coal_mine: {
        "input": 2,
        "output": 2,
    },
     industries.iron_mine: {
        "input": 2,
        "output": 2,
     },
     industries.oil_well: {
        "input": 2,
        "output": 2,
     },
 }

"""init industry config per industry"""




