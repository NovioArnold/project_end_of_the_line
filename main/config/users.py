from enum import StrEnum
from pydantic import BaseModel


"""all user rights"""
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
    set_is_ready_flag = 'set_is_ready_flag'
    set_is_occupied_flag = 'set_is_occupied_flag'
    set_is_routed_flag = 'set_is_routed_flag'
    set_is_in_service_flag = 'set_is_in_service_flag'
    set_is_assigned_to_consist_flag = 'set_is_assigned_to_consist_flag'

"""init config classes"""
RADIO = ConfigRadio
TIMETABLE = ConfigTimetable
SWITCH_LIST = ConfigSwitchList
CONSIST_TABLE = ConfigConsistTable
ITEM_MANAGER = ConfigItemManager
LOAD_UNLOAD = ConfigLoadUnload
FLAGS = ConfigFlags


class ConfigUser(BaseModel):
    """this is the users rights base model"""
    radio_rights: dict[RADIO:bool] = {
        RADIO.train_radio: False,
        RADIO.dispatch_radio: False,
        RADIO.prio_speaker: False,
        RADIO.crew_lounge: False,
        RADIO.create_train_radio: False,
        RADIO.delete_train_radio: False,
    }
    timetable_rights: dict[TIMETABLE:bool] = {
        TIMETABLE.view_timetable: False,
        TIMETABLE.delete_timetable: False,
        TIMETABLE.create_timetable: False,
        TIMETABLE.update_timetable: False,
    }
    switch_list_rights: dict[SWITCH_LIST:bool] = {
        SWITCH_LIST.create_switch_list: False,
        SWITCH_LIST.view_switch_list: False,
        SWITCH_LIST.update_switch_list: False,
        SWITCH_LIST.delete_switch_list: False,
    }
    consist_table_rights: dict[CONSIST_TABLE:bool] = {
        CONSIST_TABLE.create_consist_table: False,
        CONSIST_TABLE.view_consist_table: False,
        CONSIST_TABLE.update_consist_table: False,
        CONSIST_TABLE.delete_consist_table: False,
    }
    item_manager_rights: dict[ITEM_MANAGER:bool] = {
        ITEM_MANAGER.create_item: False,
        ITEM_MANAGER.view_item: False,
        ITEM_MANAGER.update_item: False,
        ITEM_MANAGER.delete_item: False,
    }
    load_unload_rights: dict[LOAD_UNLOAD:bool] = {
        LOAD_UNLOAD.load_car: False,
        LOAD_UNLOAD.unload_car: False,
        LOAD_UNLOAD.view_load: False,
    }
    flags_rights: dict[FLAGS:bool] = {
        FLAGS.set_derail_flag: False,
        FLAGS.set_is_ready_flag: False,
        FLAGS.set_is_occupied_flag: False,
        FLAGS.set_is_routed_flag: False,
        FLAGS.set_is_in_service_flag: False,
        FLAGS.set_is_assigned_to_consist_flag: False,
    }

