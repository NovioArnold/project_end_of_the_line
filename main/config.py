# Desc: Configuration file for project buffer
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from enum import StrEnum


""" List of all the railroads on the map"""
railroads: list[str:dict[str:str]] = [
    {
        'name': 'Canadian National',
        'road_number_prefix': 'CN',
    },
    {
        'name': 'Alaska Railroad',
        'road_number_prefix': 'ARR',
    },
    {
        'name': 'Arnold Lumber Company',
        'road_number_prefix': 'ALC',
    },

]

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


class RollinStock(StrEnum):
    """ All the types of rolling stock"""
    locomotive = 'locomotive'
    car = 'car'
    caboose = 'caboose'


class AssetUrl(StrEnum):
    """
    All the logs, documentation, maps and rulebook.
    Sets up all s3 endpoints

    """
    dispatcher_schematic_cn = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_cn.png'
    dispatcher_schematic_arr = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_arr.png'
    dispatcher_schematic_alc = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_alc.png'
    loging_camp = 'https://railroad-dispatcher.s3.amazonaws.com/logging_camp.png'
    sawmill = 'https://railroad-dispatcher.s3.amazonaws.com/sawmill.png'
    iron_mine = 'https://railroad-dispatcher.s3.amazonaws.com/iron_mine.png'
    smelter = 'https://railroad-dispatcher.s3.amazonaws.com/smelter.png'
    coal_mine = 'https://railroad-dispatcher.s3.amazonaws.com/coal_mine.png'
    steel_mill = 'https://railroad-dispatcher.s3.amazonaws.com/steel_mill.png'
    oil_well = 'https://railroad-dispatcher.s3.amazonaws.com/oil_well.png'
    oil_refinery = 'https://railroad-dispatcher.s3.amazonaws.com/oil_refinery.png'
    freight_depot = 'https://railroad-dispatcher.s3.amazonaws.com/freight_depot.png'
    # rulebooks
    cn_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/cn_rulebook.pdf'
    arr_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/arr_rulebook.pdf'
    alc_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/alc_rulebook.pdf'
    # maps
    cn_map = 'https://railroad-dispatcher.s3.amazonaws.com/cn_map.png'
    arr_map = 'https://railroad-dispatcher.s3.amazonaws.com/arr_map.png'
    alc_map = 'https://railroad-dispatcher.s3.amazonaws.com/alc_map.png'
    # logs
    operations_log = 'https://railroad-dispatcher.s3.amazonaws.com/operations_log.csv'
    db_log = 'https://railroad-dispatcher.s3.amazonaws.com/db_log.csv'
    chat_log = 'https://railroad-dispatcher.s3.amazonaws.com/chat_log.csv'
    status_log = 'https://railroad-dispatcher.s3.amazonaws.com/status_log.csv'


# the products transported on the railroad
class Products(StrEnum):
    logs = 'logs'
    lumber = 'lumber'
    beams = 'beams'
    cordwood = 'cordwood'
    iron_ore = 'iron_ore'
    raw_iron = 'raw_iron'
    rails = 'rails'
    coal = 'coal'
    pipe = 'pipe'
    tools = 'tools'
    crude_oil = 'crude_oil'
    oil_barrel = 'oil_barrel'
    wood = 'wood'
    water = 'water'
    sand = 'sand'

# Switching yards on the railroad
class Yards(StrEnum):
    freight_depot = 'freight_depot'
    sawmill_interchange = 'sawmill_interchange'
    oil_field_yard = 'oil_field_yard'
    oil_refinery_yard = 'oil_refinery_yard'
    smelter_yard = 'smelter_yard'
    mine_yard = 'mine_yard'

# Mainline junctions on te railroad
class Junctions(StrEnum):
    sawmill_junction = 'sawmill_junction'
    mine_junction = 'mine_junction'

# Type of industries on the railroad.
class Industries(StrEnum):
    logging_camp = 'Logging Camp'
    sawmill = 'Sawmill'
    iron_mine = 'Iron Mine'
    smelter = 'Smelter'
    coal_mine = 'Coal Mine'
    steel_mill = 'Steel Mill'
    oil_well = 'Oil Well'
    oil_refinery = 'Oil Refinery'


class CarTypes(StrEnum):
    """ All the types of cars on the railroad """
    flatcar = 'flatcar'
    stake_flatcar = 'stake flatcar'
    bulkhead_flatcar = 'bulkhead flatcar'
    hopper = 'hopper'
    tank_car = 'tank car'
    boxcar = 'boxcar'
    caboose = 'caboose'

#
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
    product_1: Optional[str]
    load_1: int = Field(default=0)
    product_2: Optional[str]
    load_2: int = Field(default=0)


class IndustryConfig(BaseModel):
    input_1: Optional[str] = None
    stock_input_1: int = Field(default=0)
    max_store_input_1: int = Field(default=0)
    input_2: Optional[str] = None
    stock_input_2: int = Field(default=0)
    max_store_input_2: int = Field(default=0)
    input_3: Optional[str] = None
    stock_input_3: int = Field(default=0)
    max_store_input_3: int = Field(default=0)
    output_1: Optional[str] = None
    stock_output_1: int = Field(default=0)
    max_store_output_1: int = Field(default=0)
    output_2: Optional[str] = None
    stock_output_2: int = Field(default=0)
    max_store_output_2: int = Field(default=0)
    output_3: Optional[str] = None
    stock_output_3: int = Field(default=0)
    max_store_output_3: int = Field(default=0)
    output_4: Optional[str] = None
    stock_output_4: int = Field(default=0)
    max_store_output_4: int = Field(default=0)
    output_5: Optional[str] = None
    stock_output_5: int = Field(default=0)
    max_store_output_5: int = Field(default=0)
    output_6: Optional[str] = None
    stock_output_6: int = Field(default=0)
    max_store_output_6: int = Field(default=0)
    output_7: Optional[str] = None
    stock_output_7: int = Field(default=0)
    max_store_output_7: int = Field(default=0)
    output_8: Optional[str] = None
    stock_output_8: int = Field(default=0)
    max_store_output_8: int = Field(default=0)
    output_9: Optional[str] = None
    stock_output_9: int = Field(default=0)
    max_store_output_9: int = Field(default=0)
    output_10: Optional[str] = None
    stock_output_10: int = Field(default=0)
    max_store_output_10: int = Field(default=0)
    output_11: Optional[str] = None
    stock_output_11: int = Field(default=0)
    max_store_output_11: int = Field(default=0)
    output_12: Optional[str] = None
    stock_output_12: int = Field(default=0)
    max_store_output_12: int = Field(default=0)
    output_13: Optional[str] = None
    stock_output_13: int = Field(default=0)
    max_store_output_13: int = Field(default=0)
    production_ratio: Optional[dict[str:int]] = None




car = CarTypes
load = Products
industries = Industries
production_ratio: dict[str:dict[str:int]] = {
     industries.sawmill: {
        "input": 2,
        "output": 2,
     },
     industries.smelter: {
        "input": 2,
        "output": 2,
     },
     industries.logging_camp: {
        "input": 2,
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


car.flatcar = CarConfig(procuct_1=load.logs, load_1=8, product_2=load.pipe, load_2=6)
car.stake_flatcar = CarConfig(product_1=load.lumber, load_1=8, product_2=load.beams, load_2=6)
car.bulkhead_flatcar = CarConfig(product_1=load.cordwood, load_1=8, product_2=load.oil_barrel, load_2=6)
car.hopper = CarConfig(product_1=load.coal, load_1=8, product_2=load.iron_ore, load_2=6)
car.boxcar = CarConfig(product_1=load.tools, load_1=8, product_2=None, load_2=0)
car.tank_car = CarConfig(product_1=load.crude_oil, load_1=8, product_2=None, load_2=0)
car.caboose = CarConfig(product_1=None, load_1=0, product_2=None, load_2=0)

industries.logging_camp = IndustryConfig(
    output_1=load.logs,
    stock_output_1=100,
    max_store_output_1=100,
    output_2=load.cordwood,
    stock_output_2=100,
    max_store_output_2=100,
    production_ratio=production_ratio[industries.logging_camp],
)
industries.sawmill = IndustryConfig(
    input_1=load.logs,
    stock_input_1=0,
    max_store_input_1=100,
    output_1=load.lumber,
    stock_output_1=0,
    max_store_output_1=100,
    output_2=load.beams,
    stock_output_2=0,
    max_store_output_2=100,
    production_ratio=production_ratio[industries.sawmill],
)
industries.iron_mine = IndustryConfig(
    input_1=load.beams,
    stock_input_1=0,
    max_store_input_1=30,
    input_2=load.lumber,
    stock_input_2=0,
    max_store_input_2=50,
    output_1=load.iron_ore,
    stock_output_1=0,
    max_store_output_1=1000,
    production_ratio=production_ratio[industries.iron_mine],
)
industries.smelter = IndustryConfig(
    input_1=load.iron_ore,
    stock_input_1=0,
    max_store_input_1=1000,
    input_2=load.cordwood,
    stock_input_2=0,
    max_store_input_2=1000,
    output_1=load.raw_iron,
    stock_output_1=0,
    max_store_output_1=1000,
    output_2=load.rails,
    stock_output_2=0,
    max_store_output_2=1000,
    production_ratio=production_ratio[industries.smelter],
)
industries.coal_mine = IndustryConfig(
    input_1=load.rails,
    stock_input_1=0,
    max_store_input_1=1000,
    input_2=load.beams,
    stock_input_2=0,
    max_store_input_2=1000,
    output_1=load.coal,
    stock_output_1=0,
    max_store_output_1=1000,
    production_ratio=production_ratio[industries.coal_mine],
)
industries.steel_mill = IndustryConfig(
    input_1=load.raw_iron,
    stock_input_1=0,
    max_store_input_1=1000,
    input_2=load.coal,
    stock_input_2=0,
    max_store_input_2=1000,
    input_3=load.lumber,
    stock_input_3=0,
    max_store_input_3=1000,
    output_1=load.pipe,
    stock_output_1=0,
    max_store_output_1=1000,
    output_2=load.tools,
    stock_output_2=0,
    max_store_output_2=1000,
    production_ratio=production_ratio[industries.steel_mill],
)
industries.oil_well = IndustryConfig(
    input_1=load.tools,
    stock_input_1=0,
    max_store_input_1=1000,
    input_2=load.pipe,
    stock_input_2=0,
    max_store_input_2=1000,
    input_3=load.beams,
    stock_input_3=0,
    max_store_input_3=1000,
    output_1=load.crude_oil,
    stock_output_1=0,
    max_store_output_1=1000
)
industries.oil_refinery = IndustryConfig(
    input_1=load.crude_oil,
    stock_input_1=0,
    max_store_input_1=1000,
    input_2=load.lumber,
    stock_input_2=0,
    max_store_input_2=1000,
    input_3=load.pipe,
    stock_input_3=0,
    max_store_input_3=1000,
    output_1=load.oil_barrel,
    stock_output_1=0,
    max_store_output_1=1000
)
industries.freight_depot = IndustryConfig(
    input_1=load.logs,
    stock_input_1=0,
    max_store_input_1=1000,
    input_2=load.lumber,
    stock_input_2=0,
    max_store_input_2=1000,
    input_3=load.beams,
    stock_input_3=0,
    max_store_input_3=1000,
    input_4=load.cordwood,
    stock_input_4=0,
    max_store_input_4=1000,
    input_5=load.iron_ore,
    stock_input_5=0,
    max_store_input_5=1000,
    input_6=load.raw_iron,
    stock_input_6=0,
    max_store_input_6=1000,
    input_7=load.rails,
    stock_input_7=0,
    max_store_input_7=1000,
    input_8=load.coal,
    stock_input_8=0,
    max_store_input_8=1000,
    input_9=load.pipe,
    stock_input_9=0,
    max_store_input_9=1000,
    input_10=load.tools,
    stock_input_10=0,
    max_store_input_10=1000,
    input_11=load.crude_oil,
    stock_input_11=0,
    max_store_input_11=1000,
    input_12=load.oil_barrel,
    stock_input_12=0,
    max_store_input_12=1000,
)

track_sections = {
    "template_track": {
        "name": 'freight_depot <-> lumbermill junction',
        "map": asset_url['dispatcher_schematic_cn'],
        "number_of_tracks": 1,
        "tracks": {
            "track_1": {
                "name": "fd-lmj",
                "track_id": 1,
                "track_type": track_types['mainline'],
                "occupied": False,
                "num_cars": 0,
                "max_cars": 98
            },
        },
    },
}

#  All the industries configs

""" Crew settings"""
crew_config = {
    'radio': ['train_radio', 'dispatch_radio', 'prio_speaker', 'crew_lounge', 'create_train_radio', 'delete_train_radio'],
    'timetable': ['view_timetable', 'delete_timetable', 'create_timetable', 'update_timetable'],
    'switch_list': ['create_switch_list', 'view_switch_list', 'update_switch_list', 'delete_switch_list'],
    'consist_table': ['create_consist_table', 'view_consist_table', 'update_consist_table', 'delete_consist_table'],
    'item_manager': ['create_item', 'view_item', 'update_item', 'delete_item', 'set_rail_flag',
                     'set_out_of_service_flag'],
    'load_unload': ['load_car', 'unload_car']
}

class ConfigCats(StrEnum):
    """ All the categories of config"""
    radio = 'radio'
    timetable = 'timetable'
    switch_list = 'switch_list'
    consist_table = 'consist_table'
    item_manager = 'item_manager'
    load_unload = 'load_unload'
    flags = 'flags'

class ConfigRadio(StrEnum):
    """ All the radio config"""
    train_radio = 'train_radio'
    dispatch_radio = 'dispatch_radio'
    prio_speaker = 'prio_speaker'
    crew_lounge = 'crew_lounge'
    create_train_radio = 'create_train_radio'
    delete_train_radio = 'delete_train_radio'


class ConfigTimetable(StrEnum):
    """ All the timetable config"""
    view_timetable = 'view_timetable'
    delete_timetable = 'delete_timetable'
    create_timetable = 'create_timetable'
    update_timetable = 'update_timetable'


class ConfigSwitchList(StrEnum):
    """ All the switch list config"""
    create_switch_list = 'create_switch_list'
    view_switch_list = 'view_switch_list'
    update_switch_list = 'update_switch_list'
    delete_switch_list = 'delete_switch_list'


class ConfigConsistTable(StrEnum):
    """ All the consist table config"""
    create_consist_table = 'create_consist_table'
    view_consist_table = 'view_consist_table'
    update_consist_table = 'update_consist_table'
    delete_consist_table = 'delete_consist_table'


class ConfigItemManager(StrEnum):
    """ All the item manager config"""
    create_item = 'create_item'
    view_item = 'view_item'
    update_item = 'update_item'
    delete_item = 'delete_item'


class ConfigLoadUnload(StrEnum):
    """ All the load unload config"""
    load_car = 'load_car'
    unload_car = 'unload_car'


class ConfigFlags(StrEnum):
    """ All the flags config"""
    set_derail_flag = 'set_rail_flag'
    set_is_occupied_flag = 'set_is_occupied_flag'
    set_is_routed_flag = 'set_is_routed_flag'
    set_is_in_service_flag = 'set_is_in_service_flag'
    set_is_assigned_to_consist_flag = 'set_is_assigned_to_consist_flag'


config_cat = ConfigCats
config_radio = ConfigRadio
config_timetable = ConfigTimetable
config_switch_list = ConfigSwitchList
config_consist_table = ConfigConsistTable
config_item_manager = ConfigItemManager
config_load_unload = ConfigLoadUnload
config_flags = ConfigFlags


conductor_config = {
        config_cat.radio: {
            config_radio.train_radio: True,  # train radio
            config_radio.dispatch_radio: True,  # dispatch radio
            config_radio.prio_speaker: False,  # prio speaker
            config_radio.crew_lounge: True,  # crew lounge
            config_radio.create_train_radio: True,  # create train radio
            config_radio.delete_train_radio: True,  # delete train radio
        },
        config_cat.timetable: {
            config_timetable.view_timetable: True,  # view timetable
            config_timetable.delete_timetable: True,  # delete timetable
            config_timetable.create_timetable: True,  # create timetable
            config_timetable.update_timetable: True,  # update timetable
        },
        config_cat.switch_list: {
            config_switch_list.create_switch_list: True,  # create switch list
            config_switch_list.view_switch_list: True,  # view switch list
            config_switch_list.update_switch_list: True,  # update switch list
            config_switch_list.delete_switch_list: True,  # delete switch list

        },
        config_cat.consist_table: {
            config_consist_table.create_consist_table: True,  # create consist table
            config_consist_table.view_consist_table: True,  # view consist table
            config_consist_table.update_consist_table: True,  # update consist table
            config_consist_table.delete_consist_table: True,  # delete consist table
        },
        config_cat.load_unload: {
            config_load_unload.load_car: True,  # load car
            config_load_unload.unload_car: True,  # unload car
        },
        config_cat.item_manager: {
            config_item_manager.create_item: True,  # create item
            config_item_manager.view_item: True,  # view item
            config_item_manager.update_item: True,  # update item
            config_item_manager.delete_item: True,  # delete item
        },
        config_cat.flags: {
            config_flags.set_is_occupied_flag: True,  #
            config_flags.set_is_routed_flag: True,
            config_flags.set_is_in_service_flag: True,
            config_flags.set_is_assigned_to_consist_flag: True,
            config_flags.set_derail_flag: True,
        },

}




