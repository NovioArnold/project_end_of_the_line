from enum import StrEnum


class Products(StrEnum):
    """ All the products that are transported on the railroad"""
    not_in_use = 'not_in_use'
    log = 'log'
    lumber = 'lumber'
    beam = 'beam'
    cordwood = 'cordwood'
    iron_ore = 'iron_ore'
    raw_iron = 'raw_iron'
    rails = 'rails'
    coal = 'coal'
    pipe = 'pipe'
    tool = 'tool'
    crude_oil = 'crude_oil'
    oil_barrel = 'oil_barrel'
    wood = 'wood'
    water = 'water'
    sand = 'sand'

