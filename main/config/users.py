from enum import StrEnum
from dataclasses import dataclass, field


class EnumJobs(StrEnum):
    no_role = 'no_role'
    conductor = 'conductor'
    engineer = 'engineer'
    dispatcher = 'dispatcher'
    admin = 'admin'


@dataclass
class RadioRights:
    train_radio: bool = field(default=False)
    dispatch_radio: bool = field(default=False)
    priority_speaker: bool = field(default=False)
    crew_lounge: bool = field(default=False)
    create_train_radio: bool = field(default=False)
    delete_train_radio: bool = field(default=False)


@dataclass
class TimetableRights:
    view_timetable: bool = False
    delete_timetable: bool = False
    create_timetable: bool = False
    update_timetable: bool = False


@dataclass
class SwitchListRights:
    create_switch_list: bool = False
    view_switch_list: bool = False
    update_switch_list: bool = False
    delete_switch_list: bool = False


@dataclass
class ConsistTableRights:
    create_consist_table: bool = False
    view_consist_table: bool = False
    update_consist_table: bool = False
    delete_consist_table: bool = False


@dataclass
class ItemManagerRights:
    view_item: bool = False
    create_item: bool = False
    update_item: bool = False
    delete_item: bool = False


@dataclass
class LoadUnloadRights:
    load_car: bool = False
    unload_car: bool = False
    view_product: bool = False


@dataclass
class FlagRights:
    set_derail_flag: bool = False
    set_is_ready_flag: bool = False
    set_is_out_of_service_flag: bool = False
    set_is_assigned_to_consist_flag: bool = False
    set_is_occupied_flag: bool = False
    set_is_routed_flag: bool = False















