# Desc: Configuration file for project buffer
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from enum import StrEnum
from variables import railroads
























#  TODO: refactor into their own files?
car = CarTypes
load = Products
industries = Industries



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

asset_url = AssetUrl
track_type = TrackTypes


class TrackSection(StrEnum):
    """config to generate track sections"""
    industrial = "industrial"
    yard = "yard"
    mainline = "mainline"
    interchange = "interchange"
    siding = "siding"
    junction = "junction"


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
    view_load = 'view_load'


class ConfigFlags(StrEnum):
    """ All the flags config"""
    set_derail_flag = 'set_rail_flag'
    set_is_occupied_flag = 'set_is_occupied_flag'
    set_is_routed_flag = 'set_is_routed_flag'
    set_is_in_service_flag = 'set_is_in_service_flag'
    set_is_assigned_to_consist_flag = 'set_is_assigned_to_consist_flag'


def config_crew(job_name: str):

    match job_name:
        case 'conductor':
            return conductor_config
        case 'engineer':
            return engineer_config
        case 'fireman':
            return brakeman_config



config_cat = ConfigCats
config_radio = ConfigRadio
config_timetable = ConfigTimetable
config_switch_list = ConfigSwitchList
config_consist_table = ConfigConsistTable
config_item_manager = ConfigItemManager
config_load_unload = ConfigLoadUnload
config_flags = ConfigFlags


""" Sets up the rights for the conductor"""
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
            config_load_unload.view_load: True,  # load car
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




