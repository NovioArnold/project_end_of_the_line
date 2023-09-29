from enum import StrEnum
from pydantic import BaseModel
from dataclasses import dataclass, Field


class Jobs(StrEnum):
    no_role = 'no_role'
    conductor = 'conductor'
    engineer = 'engineer'
    dispatcher = 'dispatcher'
    admin = 'admin'

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


@dataclass
class ConfigUser:
    """this is the users rights base model"""
    radio_rights: dict[RADIO:bool]
    timetable_rights: dict[TIMETABLE:bool]
    switch_list_rights : dict[SWITCH_LIST:bool]
    consist_table_rights: dict[CONSIST_TABLE:bool]
    item_manager_rights: dict[ITEM_MANAGER:bool]
    load_unload_rights: dict[LOAD_UNLOAD:bool]
    flags_rights: dict[FLAGS:bool]

test = ConfigUser(
    radio_rights={
        'train_radio': True,
        'dispatch_radio': True,
        'prio_speaker': True,
        'crew_lounge': True,
        'create_train_radio': True,
        'delete_train_radio': True,
    },
    timetable_rights={
        'view_timetable': True,
        'delete_timetable': True,
        'create_timetable': True,
        'update_timetable': True,
    },
    switch_list_rights={
        'create_switch_list': True,
        'view_switch_list': True,
        'update_switch_list': True,
        'delete_switch_list': True,
    },
    consist_table_rights={
        'create_consist_table': True,
        'view_consist_table': True,
        'update_consist_table': True,
        'delete_consist_table': True,
    },
    item_manager_rights={
        'create_item': True,
        'view_item': True,
        'update_item': True,
        'delete_item': True,
    },
    load_unload_rights={
        'load_car': True,
        'unload_car': True,
        'view_load': True,
    },
    flags_rights={
        'set_derail_flag': True,
        'set_is_ready_flag': True,
        'set_is_occupied_flag': True,

        'set_is_routed_flag': True,
        'set_is_in_service_flag': True,
        'set_is_assigned_to_consist_flag': True,
    },

)

print(test.radio_rights.__str__())
