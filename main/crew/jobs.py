
from main.config.users import ConfigUser


"""all the jobs on the railroad and their rights"""

"""Conductor"""
conductor_rights = ConfigUser(
    radio_rights={
        'train_radio': True,
        'dispatch_radio': True,
        'priority_speaker': False,
        'crew_lounge': True,
        'create_train_radio': False,
        'delete_train_radio': False,
    },
    timetable_rights={
        'view_timetable': True,
        'delete_timetable': False,
        'create_timetable': False,
        'update_timetable': False,

    },
    switch_list_rights={
        'create_switch_list': True,
        'view_switch_list': True,
        'update_switch_list': True,
        'delete_switch_list': False,

    },
    consist_table_rights={
        'create_consist_table': False,
        'view_consist_table': True,
        'update_consist_table': False,
        'delete_consist_table': False,
    },
    item_manager_rights={
        'view_item': True,
        'create_item': False,
        'update_item': False,
        'delete_item': False,
    },
    load_unload_rights={
        'load_car': True,
        'unload_car': True,
        'view_product': True,
    },
    flags_rights={
        'set_derail_flag': True,
        'set_is_ready_flag': True,
        'set_is_out_in_service_flag': False,
        'set_is_assigned_to_consist_flag': False,
        'set_is_occupied_flag': False,
        'set_is_routed_flag': False,
    },
)
"""Engineer"""
engineer_rights = ConfigUser(
    radio_rights={
        'train_radio': True,
        'dispatch_radio': True,
        'crew_lounge': True,
        'create_train_radio': False,
        'delete_train_radio': False,
        'priority_speaker': False,
    },
    timetable_rights={
        'view_timetable': True,
        'delete_timetable': False,
        'create_timetable': False,
        'update_timetable': False,
    },
    switch_list_rights={
        'view_switch_list': True,
        'create_switch_list': False,
        'update_switch_list': False,
        'delete_switch_list': False,

    },
    consist_table_rights={
        'view_consist_table': True,
        'create_consist_table': False,
        'update_consist_table': False,
        'delete_consist_table': False,
    },
    item_manager_rights={
        'view_item': True,
        'create_item': False,
        'update_item': False,
        'delete_item': False,
    },
    load_unload_rights={
        'load_car': True,
        'unload_car': True,
        'view_product': True,
    },
    flags_rights={
        'set_is_ready_flag': True,
        'set_is_out_in_service_flag': False,
        'set_is_assigned_to_consist_flag': False,
        'set_is_occupied_flag': False,
        'set_is_routed_flag': False,
        'set_derail_flag': False,
    },
)

"""Dispatcher"""
dispatcher_rights = ConfigUser(
    radio_rights={
        'train_radio': True,
        'dispatch_radio': True,
        'priority_speaker': True,
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
        'view_item': True,
        'create_item': False,
        'update_item': False,
        'delete_item': False,
    },
    flags_rights={
        'set_is_out_in_service_flag': True,
        'set_is_assigned_to_consist_flag': True,
        'set_is_occupied_flag': True,
        'set_is_routed_flag': True,
        'set_derail_flag': True,
        'set_is_ready_flag': True,

    },
    load_unload_rights={
        'load_car': False,
        'unload_car': False,
        'view_product': True,
    },
)

"""Admin"""
admin_rights = ConfigUser(
    radio_rights={
        'train_radio': True,
        'dispatch_radio': True,
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
        'view_product': True,
    },
    flags_rights={
        'set_is_out_in_service_flag': True,
        'set_is_assigned_to_consist_flag': True,
        'set_is_occupied_flag': True,
        'set_is_routed_flag': True,
        'set_derail_flag': True,
        'set_is_ready_flag': True,
    },
)







