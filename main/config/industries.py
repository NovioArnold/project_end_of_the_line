
from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field

from products import Products


"""init products base class"""
PRODUCT = Products


class Industries(StrEnum):
    """ All the industries on the railroad"""
    logging_camp = 'Logging Camp'
    sawmill = 'Sawmill'
    iron_mine = 'Iron Mine'
    smelter = 'Smelter'
    coal_mine = 'Coal Mine'
    steel_mill = 'Steel Mill'
    oil_well = 'Oil Well'
    oil_refinery = 'Oil Refinery'
    freight_depot = 'Freight Depot'


class IndustryConfig(BaseModel):
    """Industry input output config"""
    input_1: str = Field(default=PRODUCT.not_in_use)
    stock_input_1: int = Field(default=0)
    max_store_input_1: int = Field(default=0)
    input_2: str = Field(default=PRODUCT.not_in_use)
    stock_input_2: int = Field(default=0)
    max_store_input_2: int = Field(default=0)
    input_3: str = Field(default=PRODUCT.not_in_use)
    stock_input_3: int = Field(default=0)
    max_store_input_3: int = Field(default=0)
    output_1: str = Field(default=PRODUCT.not_in_use)
    stock_output_1: int = Field(default=0)
    max_store_output_1: int = Field(default=0)
    output_2: str = Field(default=PRODUCT.not_in_use)
    stock_output_2: int = Field(default=0)
    max_store_output_2: int = Field(default=0)
    output_3: str = Field(default=PRODUCT.not_in_use)
    stock_output_3: int = Field(default=0)
    max_store_output_3: int = Field(default=0)
    output_4: str = Field(default=PRODUCT.not_in_use)
    stock_output_4: int = Field(default=0)
    max_store_output_4: int = Field(default=0)
    output_5: str = Field(default=PRODUCT.not_in_use)
    stock_output_5: int = Field(default=0)
    max_store_output_5: int = Field(default=0)
    output_6: str = Field(default=PRODUCT.not_in_use)
    stock_output_6: int = Field(default=0)
    max_store_output_6: int = Field(default=0)
    output_7: str = Field(default=PRODUCT.not_in_use)
    stock_output_7: int = Field(default=0)
    max_store_output_7: int = Field(default=0)
    output_8: str = Field(default=PRODUCT.not_in_use)
    stock_output_8: int = Field(default=0)
    max_store_output_8: int = Field(default=0)
    output_9: str = Field(default=PRODUCT.not_in_use)
    stock_output_9: int = Field(default=0)
    max_store_output_9: int = Field(default=0)
    output_10: str = Field(default=PRODUCT.not_in_use)
    stock_output_10: int = Field(default=0)
    max_store_output_10: int = Field(default=0)
    output_11: str = Field(default=PRODUCT.not_in_use)
    stock_output_11: int = Field(default=0)
    max_store_output_11: int = Field(default=0)
    output_12: str = Field(default=PRODUCT.not_in_use)
    stock_output_12: int = Field(default=0)
    max_store_output_12: int = Field(default=0)
    output_13: str = Field(default=PRODUCT.not_in_use)
    stock_output_13: int = Field(default=0)
    max_store_output_13: int = Field(default=0)
    production_ratio: Optional[dict[production_ratio]] = Field(default_factory=dict, name="production_ratio")


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



