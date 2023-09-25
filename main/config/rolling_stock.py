from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field

from products import Products


class RollinStock(StrEnum):
    """ All the types of rolling stock"""
    locomotive = 'locomotive'
    car = 'car'
    caboose = 'caboose'


class CarTypes(StrEnum):
    """ All the types of cars on the railroad """
    flatcar = 'flatcar'
    stake_flatcar = 'stake_flatcar'
    bulkhead_flatcar = 'bulkhead_flatcar'
    hopper = 'hopper'
    tank_car = 'tank_car'
    boxcar = 'boxcar'
    caboose = 'caboose'


class LocomotiveTypes(StrEnum):
    """ All the types of locomotives on the railroad """
    porter_0_4_0 = 'porter_0-4-0'
    porter_0_4_2 = 'porter_0-2-2'
    american_4_4_0 = 'american_4-4-0'
    mogul_2_6_0 = 'mogul_2-6-0'
    consolidation_2_8_0 = 'consolidation_2-8-0'
    mikado_2_8_2 = 'mikado_2-8-2'
    hudson_4_6_4 = 'hudson_4-6-4'
    northern_4_8_4 = 'northern_4-8-4'
    shay_geared_4_4 = 'shay_geared_4-4'
    climax_geared_4_4 = 'climax_geared_4-4'


class CarConfig(BaseModel):
    """carload config"""
    product_1: str = Field(default=Products.not_in_use)
    load_1: int = Field(default=0)
    max_load_1: int = Field(default=0)
    product_2: str = Field(default=Products.not_in_use)
    load_2: int = Field(default=0)
    max_load_2: int = Field(default=0)
