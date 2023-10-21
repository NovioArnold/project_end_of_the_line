from dataclasses import dataclass, field
from enum import StrEnum


class EnumJobs(StrEnum):
    """job enumerator"""

    no_role = "no_role"
    conductor = "conductor"
    engineer = "engineer"
    dispatcher = "dispatcher"
    admin = "admin"


@dataclass
class RadioRights:
    """all radio rights (discord)"""

    train_radio: bool = False
    dispatch_radio: bool = False
    priority_speaker: bool = False
    crew_lounge: bool = False
    create_train_radio: bool = False
    delete_train_radio: bool = False


@dataclass
class TimetableRights:
    """all timetable rights"""

    view_timetable: bool = False
    delete_timetable: bool = False
    create_timetable: bool = False
    update_timetable: bool = False


@dataclass
class SwitchListRights:
    """alll switch list rights"""

    create_switch_list: bool = False
    view_switch_list: bool = False
    update_switch_list: bool = False
    delete_switch_list: bool = False


@dataclass
class ConsistTableRights:
    """all consist table rights"""

    create_consist_table: bool = False
    view_consist_table: bool = False
    update_consist_table: bool = False
    delete_consist_table: bool = False


@dataclass
class ItemManagerRights:
    """all item management rights"""

    view_item: bool = False
    create_item: bool = False
    update_item: bool = False
    delete_item: bool = False


@dataclass
class LoadUnloadRights:
    """all loading and unloading righs"""

    load_car: bool = False
    unload_car: bool = False
    view_product: bool = False


@dataclass
class FlagRights:
    """all flag rights"""

    set_derail_flag: bool = False
    set_is_ready_flag: bool = False
    set_is_out_of_service_flag: bool = False
    set_is_assigned_to_consist_flag: bool = False
    set_is_occupied_flag: bool = False
    set_is_routed_flag: bool = False
    set_is_admin: bool = False
