# This file contains all the track configuration enums on the railroad.
from enum import StrEnum


class TrackTypes(StrEnum):
    """ All the types of track"""
    mainline = 'mainline'
    siding = 'siding'
    interchange = 'interchange'
    junction = 'junction'
    switch = 'switch'
    spur = 'spur'
    service = 'service'
    lead = 'lead'
    classification = 'classification'
    departure = 'departure'
    arrival = 'arrival'


class TrackSection(StrEnum):
    """config to generate track sections"""
    industrial = "industrial"
    yard = "yard"
    mainline = "mainline"
    interchange = "interchange"
    siding = "siding"
    junction = "junction"


class Yards(StrEnum):
    """ All the yards on the railroad"""
    freight_depot = 'freight_depot'  # main shops
    sawmill_interchange = 'sawmill_interchange'  # interchange yard for ALC/CN/ARR
    oil_field_yard = 'oil_field_yard'  # main yard for Canadian National
    oil_refinery_yard = 'oil_refinery_yard'  # interchange yard for CN/ASL
    smelter_yard = 'smelter_yard'
    mine_yard = 'mine_yard'  # main yard for Alaska Railroad
    lumber_camp_yard = 'lumber_camp_yard'
    coal_mine_yard = 'coal_mine_yard'
    iron_mine_yard = 'iron_mine_yard'


# Mainline junctions on te railroad
class Junctions(StrEnum):
    """ All the junctions on the railroad"""
    sawmill_junction = 'sawmill_junction'
    mine_junction = 'mine_junction'


class Siding(StrEnum):
    """ All the sidings on the railroad"""
    freight_depot_siding = 'freight_depot_siding'
    oil_field_siding = 'oil_field_siding'
    coal_mine_siding = 'coal_mine_siding'
    iron_works_siding = 'iron_works_siding'
    refinery_siding = 'refinery_siding'


class Mainline(StrEnum):
    """
    All the mainline tracks on the railroad.
    This is for routing trains.
    """
    none = 'none'
    fdy2fds = 'fdy2fds'  # freight depot to freight depot yard siding
    fds2smj = 'fds2smj'  # freight depot yard siding to sawmill junction
    ows2smj = 'ows2smj'  # oil well siding to sawmill junction
    ows2owy = 'ows2owy'  # oil well siding to oil well yard
    smy2smj = 'smy2smj'  # sawmill yard to sawmill junction
    smy2lcy = 'smy2lcy'  # sawmill yard to lumber camp yard
    smy2mij = 'smy2mij'  # sawmill yard to mine junction
    mij2miy = 'mij2miy'  # mine junction to mine yard
    mij2sty = 'mij2sty'  # mine junction to smelter yard
    mij2cmy = 'mij2cmy'  # mine junction to coal mine yard
    miy2imy = 'miy2imy'  # mine yard to iron mine yard
    owy2iws = 'owy2iws'  # oil well yard to iron works siding
    owy2rfs = 'owy2rfs'  # oil well yard to refinery siding
    rfs2rfy = 'rfs2rfy'  # refinery siding to refinery yard


class Route(StrEnum):
    """ The routes selectable by the dispatcher"""
    """No route selected"""
    none = 'none'
    """Routes from the freight depot"""
    freight_depot_to_sawmill_yard = 'freight_depot_to_sawmill_yard'
    freight_depot_to_oil_field_yard = 'freight_depot_to_oil_field_yard'
    freight_depot_to_mine_yard = 'freight_depot_to_mine_yard'
    """Routes from the sawmill yard"""
    sawmill_yard_to_mine_yard = 'sawmill_yard_to_mine_yard'
    sawmill_yard_to_lumber_camp_yard = 'sawmill_yard_to_lumber_camp_yard'
    sawmill_yard_to_oil_field_yard = 'sawmill_yard_to_oil_field_yard'
    sawmill_yard_to_freight_depot_yard = 'sawmill_yard_to_freight_depot_yard'
    """Routs from lumber camp yard"""
    lumber_camp_yard_to_sawmill_yard = 'lumber_camp_yard_to_sawmill_yard'
    """Routs from mine yard"""
    mine_yard_to_sawmill_yard = 'mine_yard_to_sawmill_yard'
    mine_yard_to_coal_mine_yard = 'mine_yard_to_coal_mine_yard'
    mine_yard_to_smelter_yard = 'mine_yard_to_smelter_yard'
    mine_yard_to_iron_mine_yard = 'mine_yard_to_iron_mine_yard'
    """Routes from coal mine yard"""
    coal_mine_yard_to_mine_yard = 'coal_mine_yard_to_mine_yard'
    """Routes from iron mine yard"""
    iron_mine_yard_to_mine_yard = 'iron_mine_yard_to_mine_yard'
    """Routes from smelter yard"""
    smelter_yard_to_mine_yard = 'smelter_yard_to_mine_yard'
    """Routes from oil field yard"""
    oil_field_yard_to_sawmill_yard = 'oil_field_yard_to_sawmill_yard'
    oil_field_yard_to_oil_refinery_yard = 'oil_field_yard_to_oil_refinery_yard'
    oil_field_yard_to_freight_depot_yard = 'oil_field_yard_to_freight_depot_yard'
    oil_field_yard_to_ironworks = 'oil_field_yard_to_ironworks'
    """Routes from oil refinery yard"""
    oil_refinery_yard_to_oil_field_yard = 'oil_refinery_yard_to_oil_field_yard'





