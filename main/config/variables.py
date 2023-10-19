from main.config.industries import industries, PRODUCT, production_ratio
from main.config.users import EnumJobs
JOB = EnumJobs
""" List of all the railroads on the map"""
railroads: list[str:dict[str:str]] = [
    {
        'name': 'None',
        'road_number_prefix': 'none',
    },
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
    {
        'name': 'Arnold Short Line',
        'road_number_prefix': 'ASL',
    }

]

jobs = {
    JOB.conductor: {
        'name': 'conductor',
        'radio_rights': {
            'train_radio': True,
            'dispatcher_radio': True,
            'crew_lounge': True,
            'priority_speaker': False,
            'create_train_radio': False,
            'delete_train_radio': False,
        },
        'timetable_rights': {
            'view_timetable': True,
            'update_timetable': False,
            'delete_timetable': False,
            'create_timetable': False,
        },
        'switch_list_rights': {
            'view_switch_list': True,
            'update_switch_list': True,
            'delete_switch_list': False,
            'create_switch_list': False,
        },
        'consist_table_rights': {
            'view_consist_table': True,
            'update_consist_table': True,
            'delete_consist_table': False,
            'create_consist_table': False,
        },
        'item_manager_rights': {
            'view_item': True,
            'create_item': False,
            'update_item': False,
            'delete_item': False,
        },
        'load_unload_rights': {
            'load_car': True,
            'unload_car': True,
            'view_product': True,
        },
        'flag_rights': {
            'set_derail_flag': True,
            'set_is_ready_flag': True,
            'set_is_out_of_service_flag': False,
            'set_is_assigned_to_consist_flag': False,
            'set_is_occupied_flag': False,
            'set_is_routed_flag': False,

        }
    },
    JOB.engineer: {
        'name': 'engineer',
        'radio_rights': {
            'train_radio': True,
            'crew_lounge': True,
            'dispatcher_radio': False,
            'priority_speaker': False,
            'create_train_radio': False,
            'delete_train_radio': False,

        },
        'timetable_rights': {
            'view_timetable': True,
            'update_timetable': False,
            'delete_timetable': False,
            'create_timetable': False,

        },
        'switch_list_rights': {
            'view_switch_list': True,
            'update_switch_list': False,
            'delete_switch_list': False,
            'create_switch_list': False,
        },
        'consist_table_rights': {
            'view_consist_table': True,
            'update_consist_table': False,
            'delete_consist_table': False,
            'create_consist_table': False,
        },
        'item_manager_rights': {
            'view_item': True,
            'create_item': False,
            'update_item': False,
            'delete_item': False,
        },
        'load_unload_rights': {
            'load_car': True,
            'unload_car': True,
            'view_product': True,
        },
        'flag_rights': {
            'set_derail_flag': True,
            'set_is_ready_flag': True,
            'set_is_out_of_service_flag': False,
            'set_is_assigned_to_consist_flag': False,
            'set_is_occupied_flag': False,
            'set_is_routed_flag': False,
        }
    },
    JOB.dispatcher: {
        'name': 'dispatcher',
        'radio_rights': {
            'train_radio': False,
            'dispatcher_radio': True,
            'priority_speaker': True,
            'crew_lounge': True,
            'create_train_radio': True,
            'delete_train_radio': True,
        },
        'timetable_rights': {
            'view_timetable': True,
            'delete_timetable': True,
            'create_timetable': True,
            'update_timetable': True,
        },
        'switch_list_rights': {
            'view_switch_list': True,
            'delete_switch_list': True,
            'create_switch_list': True,
            'update_switch_list': True,
        },
        'consist_table_rights': {
            'view_consist_table': True,
            'delete_consist_table': True,
            'create_consist_table': True,
            'update_consist_table': True,
        },
        'item_manager_rights': {
            'view_item': True,
            'create_item': False,
            'update_item': False,
            'delete_item': False,
        },
        'flag_rights': {
            'set_is_out_of_service_flag': True,
            'set_is_ready_flag': True,
            'set_is_assigned_to_consist_flag': True,
            'set_is_occupied_flag': True,
            'set_is_routed_flag': True,
        }
    },
    JOB.admin: {
        'name': 'admin',
        'radio_rights': {
            'train_radio': True,
            'dispatcher_radio': True,
            'priority_speaker': True,
            'crew_lounge': True,
            'create_train_radio': True,
            'delete_train_radio': True,
        },
        'timetable_rights': {
            'view_timetable': True,
            'delete_timetable': True,
            'create_timetable': True,
            'update_timetable': True,
        },
        'switch_list_rights': {
            'view_switch_list': True,
            'delete_switch_list': True,
            'create_switch_list': True,
            'update_switch_list': True,
        },
        'consist_table_rights': {
            'view_consist_table': True,
            'delete_consist_table': True,
            'create_consist_table': True,
            'update_consist_table': True,
        },
        'item_manager_rights': {
            'view_item': True,
            'create_item': True,
            'update_item': True,
            'delete_item': True,
        },
        'load_unload_rights': {
            'load_car': True,
            'unload_car': True,
            'view_product': True,
        },
        'flag_rights': {
            'set_derail_flag': True,
            'set_is_ready_flag': True,
            'set_is_out_of_service_flag': True,
            'set_is_assigned_to_consist_flag': True,
            'set_is_occupied_flag': True,
            'set_is_routed_flag': True,
        }
    },
    JOB.no_role: {
        'name': 'no_role',
        'radio_rights': {
            'crew_lounge': True,
            'train_radio': False,
            'dispatcher_radio': False,
            'priority_speaker': False,
            'create_train_radio': False,
            'delete_train_radio': False,

        },
        'timetable_rights': {
            'view_timetable': False,
            'delete_timetable': False,
            'create_timetable': False,
            'update_timetable': False,
        },
        'switch_list_rights': {
            'view_switch_list': False,
            'delete_switch_list': False,
            'create_switch_list': False,
            'update_switch_list': False,
        },
        'consist_table_rights': {
            'view_consist_table': False,
            'delete_consist_table': False,
            'create_consist_table': False,
            'update_consist_table': False,
        },
        'item_manager_rights': {
            'view_item': False,
            'create_item': False,
            'update_item': False,
            'delete_item': False,
        },
        'load_unload_rights': {
            'load_car': False,
            'unload_car': False,
            'view_product': False,
        },
        'flag_rights': {
            'set_derail_flag': False,
            'set_is_ready_flag': False,
            'set_is_out_of_service_flag': False,
            'set_is_assigned_to_consist_flag': False,
            'set_is_occupied_flag': False,
            'set_is_routed_flag': False,
        }
    }
}

"""industry config"""

industry_config: dict[industries] = {
    industries.sawmill: {
        "input_1": PRODUCT.log,
        "stock_input_1": 0,
        "max_store_input_1": 1000,
        "output_1": PRODUCT.lumber,
        "stock_output_1": 0,
        "max_store_output_1": 100,
        "output_2": PRODUCT.beam,
        "stock_output_2": 0,
        "max_store_output_2": 100,
        "production_ratio": production_ratio[industries.sawmill],

    },
    industries.smelter: {
        "input_1": PRODUCT.iron_ore,
        "stock_input_1": 0,
        "max_store_input_1": 1000,
        "input_2": PRODUCT.coal,
        "stock_input_2": 0,
        "max_store_input_2": 1000,
        "output_1": PRODUCT.raw_iron,
        "stock_output_1": 0,
        "max_store_output_1": 100,
        "output_2": PRODUCT.rails,
        "stock_output_2": 0,
        "max_store_output_2": 100,
        "production_ratio": production_ratio[industries.smelter],
    },
    industries.logging_camp: {
        "output_1": PRODUCT.log,
        "stock_output_1": 0,
        "max_store_output_1": 100,
        "output_2": PRODUCT.cordwood,
        "stock_output_2": 0,
        "max_store_output_2": 100,
    },
    industries.oil_refinery: {
        "input_1": PRODUCT.crude_oil,
        "stock_input_1": 0,
        "max_store_input_1": 1000,
        "input_2": PRODUCT.lumber,
        "stock_input_2": 0,
        "max_store_input_2": 1000,
        "input_3": PRODUCT.pipe,
        "stock_input_3": 0,
        "max_store_input_3": 1000,
        "output_1": PRODUCT.oil_barrel,
        "stock_output_1": 0,
        "max_store_output_1": 100,
        "output_2": PRODUCT.tool,
        "stock_output_2": 0,
        "max_store_output_2": 100,
        "production_ratio": production_ratio[industries.oil_refinery],
    },
    industries.coal_mine: {
        "input_1": PRODUCT.beam,
        "stock_input_1": 0,
        "max_store_input_1": 1000,
        "input_2": PRODUCT.rails,
        "stock_input_2": 0,
        "max_store_input_2": 1000,
        "output_1": PRODUCT.coal,
        "stock_output_1": 0,
        "max_store_output_1": 100,
        "production_ratio": production_ratio[industries.coal_mine],
    },
    industries.iron_mine: {
        "input_1": PRODUCT.lumber,
        "stock_input_1": 0,
        "max_store_input_1": 1000,
        "input_2": PRODUCT.beam,
        "stock_input_2": 0,
        "max_store_input_2": 1000,
        "output_1": PRODUCT.iron_ore,
        "stock_output_1": 0,
        "max_store_output_1": 100,
        "production_ratio": production_ratio[industries.iron_mine],
    },
    industries.oil_well: {
        "input_1": PRODUCT.beam,
        "stock_input_1": 0,
        "max_store_input_1": 1000,
        "input_2": PRODUCT.pipe,
        "stock_input_2": 0,
        "max_store_input_2": 1000,
        "input_3": PRODUCT.tool,
        "stock_input_3": 0,
        "max_store_input_3": 1000,
        "output_1": PRODUCT.crude_oil,
        "stock_output_1": 0,
        "max_store_output_1": 100,
        "production_ratio": production_ratio[industries.oil_well],
    },
}

location = [
    'none',
    'freight_depot',
    'sawmill',
    'smelter',
    'logging_camp',
    'oil_refinery',
    'coal_mine',
    'iron_mine',
    'oil_well',
]
