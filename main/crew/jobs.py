
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

"""Dispatcher"""
dispatcher_rights = ConfigUser(
    radio={
        'train_radio': True,
        'dispatch_radio': True,
        'crew_lounge': True,
        'create_train_radio': True,
        'delete_train_radio': True,
    },
    timetable={
        'view_timetable': True,
        'delete_timetable': True,
        'create_timetable': True,
        'update_timetable': True,
    },
    switch_list={
        'create_switch_list': True,
        'view_switch_list': True,
        'update_switch_list': True,
        'delete_switch_list': True,
    },
    consist_table={
        'create_consist_table': True,
        'view_consist_table': True,
        'update_consist_table': True,
        'delete_consist_table': True,
    },
    item_manager={
        'view_item': True,
    },
    flags={
        'set_is_out_in_service_flag': True,
        'set_is_assigned_to_consist_flag': True,
        'set_is_occupied_flag': True,
        'set_is_routed_flag': True,
        'set_derail_flag': True,
        'set_is_ready_flag': True,

    },
)






