
from main.config.users import ConfigUser


"""all the jobs on the railroad and their rights"""
"""Conductor"""
conductor_rights = ConfigUser(
    radio={
        'train_radio': True,
        'dispatch_radio': True,
        'crew_lounge': True,
    },
    timetable={
        'view_timetable': True,
    },
    switch_list={
        'view_switch_list': True,
        'update_switch_list': True,
    },
    consist_table={
        'view_consist_table': True,
    },
    item_manager={
        'view_item': True,
    },
    load_unload={
        'load_car': True,
        'unload_car': True,
        'view_product': True,
    },
    flags={
        'set_derail_flag': True,
        'set_is_ready_flag': True,
    },
)
"""Engineer"""
engineer_rights = ConfigUser(
    radio={
        'train_radio': True,
        'dispatch_radio': True,
        'crew_lounge': True,
    },
    timetable={
        'view_timetable': True,
    },
    switch_list={
        'view_switch_list': True,
    },
    consist_table={
        'view_consist_table': True,
    },
    item_manager={
        'view_item': True,
    },
    load_unload={
        'load_car': True,
        'unload_car': True,
        'view_product': True,
    },
    flags={
        'set_is_ready_flag': True,
    },
)





