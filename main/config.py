# Desc: Configuration file for project buffer
from typing import List, Dict, Optional
from pydantic import BaseModel, Field

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

""" All the typ of tracks"""
track_types: dict[str:str] = {
    'mainline': 'mainline',
    'yard_lead': 'yard_lead',
    'yard_arrival': 'yard_arrival',
    'yard_departure': 'yard_departure',
    'yard_classification': 'yard_classification',
    'siding': 'siding',
    'spur': 'spur',
    'industrial_lead': 'industrial_lead',
    'industrial_loading': 'industrial_loading',
    'industrial_unloading': 'industrial_unloading',
    'interchange': 'interchange',
    'wye': 'wye',
    'junction': 'junction',
    'service': 'service',
}

""" All the types of rolling stock"""
type_rolling_stock: dict[str:str] = {
    'engine': 'engine',
    'car': 'car',
    'caboose': 'caboose',
}

""" 
All the logs, documentation, maps and rulebook.
Sets up all s3 endpoints

"""
asset_url: dict[str:str] = {
    # Maps
    'lumber_camp': './maps/lumber_camp.pdf',
    'sawmill': './maps/sawmill.pdf',
    'iron_mine': './maps/iron_mine.pdf',
    'smelter': './maps/smelter.pdf',
    'coal_mine': './maps/coal_mine.pdf',
    'steel_mill': './maps/steel_mill.pdf',
    'oil_well': './maps/oil_well.pdf',
    'oil_refinery': './maps/oil_refinery.pdf',
    'freight_depot': './maps/freight_depot.pdf',
    'dispatcher_schematic_arr': './maps/dispatcher_schematic_arr.pdf',
    'dispatcher_schematic_cn': './maps/dispatcher_schematic_cn.pdf',
    'sawmill_interchange': '/maps/sawmill_interchange.pdf',
    'oil_field_yard': '/maps/oil_field_yard.pdf',
    'smelter_yard': '/maps/smelter_yard.pdf',
    'mine_yard': '/maps/mine_yard.pdf',
    'sawmill_junction': '/maps/sawmill_junction.pdf',
    'mine_junction': '/maps/mine_junction.pdf',
    # Rulebook
    'mainline_operations': './rules/mainline_ops.pdf',
    # Documentation
    'drivers_manual': './manual/drivers_manual.pdf',
    # Logbook
    'server_logs': './logs/server_logs.csv'
}

# the products transported on the railroad
products: dict[str:str] = {
    'logs': 'logs',
    'cordwood': 'cordwood',
    'lumber': 'lumber',
    'beams': 'beams',
    'iron_ore': 'iron_ore',
    'raw_iron': 'raw_iron',
    'rails': 'rails',
    'coal': 'coal',
    'pipe': 'pipe',
    'tools': 'tools',
    'crude_oil': 'crude_oil',
    'oil_barrel': 'oil_barrel',
}

# Switching yards on the railroad
yards: dict[str:str] = {
    'freight_depot': 'freight_depot',
    'sawmill_interchange': 'sawmill_interchange',
    'oil_field_yard': 'oil_field_yard',
    'smelter_yard': 'smelter_yard',
    'mine_yard': 'mine_yard',
}

# Mainline junctions on te railroad
junctions: dict[str:str] = {
    'sawmill_junction': 'sawmill_junction',
    'mine_junction': 'mine_junction',
}

# Type of industries on the railroad.
industries: dict[str:str] = {
    "Logging Camp": 'loging_camp',
    "Sawmill": 'sawmill',
    "Iron Mine": 'iron_mine',
    "Smelter": 'smelter',
    "Coal Mine": 'coal_mine',
    "Steel Mill":  'steel_mill',
    "Oil Well": 'oil_well',
    "Oil Refinery": 'oil_refinery',
    "Freight Depot": 'freight_depot',
}

# Type of cars on the railroad
cars: dict[str:str] = {
    "flatcar": "flatcar",
    "stake_flatcar": "stake flatcar",
    "bulkhead_flatcar": "bulkhead flatcar",
    "hopper": "hopper",
    "tank_car": "tank car",
    "boxcar": "boxcar",
    "caboose": "caboose",
}

#
engine: dict[str:str] = {
    'porter-0-4-0': 'porter-0-4-0',
    'american-4-4-0': 'american-4-4-0',
    'mogul-2-6-0': 'mogul-2-6-0',
    'ten-wheeler-4-6-0': 'ten-wheeler-4-6-0',
    'consolidation-2-8-0': 'consolidation-2-8-0',
    'mikado-2-8-2': 'mikado-2-8-2',
    'mountain-4-8-2': 'mountain-4-8-2',
    'northern-4-8-4': 'northern-4-8-4',
    'hudson-4-6-4': 'hudson-4-6-4',
    'challenger-4-6-6-4': 'challenger-4-6-6-4',
    'climax-geared': 'climax-geared',
    'shay-geared': 'shay-geared',
    'heisler-geared': 'heisler-geared',
    'switcher-0-6-0': 'switcher-0-6-0',
}


production_ratio: dict[str:dict[str:int]] = {
     "sawmill": {
        "input": 2,
        "output": 2,
     },
     "smetler": {
        "input": 2,
        "output": 2,
     },
     "steel_mill": {
        "input": 2,
        "output": 2,
     },
     "oil_refinery": {
        "input": 2,
        "output": 2,
     },
     "coal_mine": {
        "input": 2,
        "output": 2,
    },
     "iron_mine": {
        "input": 2,
        "output": 2,
     },
     "oil_well": {
        "input": 2,
        "output": 2,
     },
 }

car_load: dict[str:dict[str:tuple[str, int]]] = {
    "flatcar": {
        "load_1": ("Logs", 8),
        "load_2": ("pipe", 6)
    },
    "stake_car": {
        "load_1": ("lumber", 6),
        "load_2": ("beams", 3),
    },
    "bulkhead_flatcar": {
        "load_1": ("cordwood", 8),
        "load_2": ("oil_barrel", 6),
    },
    "hopper": {
        "load_1": ("coal", 8),
        "load_2": ("iron_ore", 6),

    },
    "tank_car": {
        "load_1": ("crude_oil", 8),
        "load_2": (None, 0),
    },
    "boxcar": {
        "load_1": ("tools", 8),
        "load_2": (None, 0),
    },
    "caboose": {
        "load_1": (None, 0),
        "load_2": (None, 0),
    },
}

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
loging_camp = {
    "name": industries['Logging Camp'],
    "map": asset_url['lumber_camp'],
    "output_1": products['logs'],
    "stock_output_1": 100,
    "max_store_output_1": 100,
    "output_2": products['cordwood'],
    "stock_output_2": 100,
    "max_store_output_2": 100,
}

sawmill = {
    "name": industries['Sawmill'],
    "map": asset_url['sawmill'],
    "input_1": products['logs'],
    "stock_input_1": 0,
    "max_store_input_1": 100,
    "output_1": products['lumber'],
    "stock_output_1": 0,
    "max_store_output_1": 100,
    "output_2": products['beams'],
    "stock_output_2": 0,
    "max_store_output_2": 100,
    "ratio": production_ratio['sawmill'],
}

iron_mine = {
    "name": industries['Iron Mine'],
    "map": asset_url['iron_mine'],
    "input_1": products['beams'],
    "stock_input_1": 0,
    "max_store_input_1": 30,
    "input_2": products['lumber'],
    "stock_input_2": 0,
    "max_store_input_2": 50,
    "output_1": products['iron_ore'],
    "stock_output_1": 0,
    "max_store_output_1": 1000,
    "ratio": production_ratio['iron_mine'],
}

smelter = {
    "name": industries['Smelter'],
    "map": asset_url['smelter'],
    "input_1": products['iron_ore'],
    "stock_input_1": 0,
    "max_store_input_1": 1000,
    "input_2": products['cordwood'],
    "stock_input_2": 0,
    "max_store_input_2": 1000,
    "output_1": products['raw_iron'],
    "stock_output_1": 0,
    "max_store_output_1": 1000,
    "output_2": products['rails'],
    "stock_output_2": 0,
    "max_store_output_2": 1000,
    "ratio": production_ratio['smelter'],
}

coal_mine = {
    "name": industries['Coal Mine'],
    "map": asset_url['coal_mine'],
    "input_1": products['rails'],
    "stock_input_1": 0,
    "max_store_input_1": 1000,
    "input_2": products['beams'],
    "stock_input_2": 0,
    "max_store_input_2": 1000,
    "output_1": products['coal'],
    "stock_output_1": 0,
    "max_store_output_1": 1000,
    "ratio": production_ratio['coal_mine'],
}

steel_mill = {
    "name": industries['Steel Mill'],
    "map": asset_url['steel_mill'],
    "input_1": products['raw_iron'],
    "stock_input_1": 0,
    "max_store_input_1": 1000,
    "input_2": products['coal'],
    "stock_input_2": 0,
    "max_store_input_2": 1000,
    "input_3": products['lumber'],
    "stock_input_3": 0,
    "max_store_input_3": 1000,
    "output_1": products['pipe'],
    "stock_output_1": 0,
    "max_store_output_1": 1000,
    "output_2": products['tools'],
    "stock_output_2": 0,
    "max_store_output_2": 1000,
    "ratio": production_ratio['steel_mill'],
}

oil_well = {
    "name": industries['Oil Well'],
    "map": asset_url['oil_well'],
    "input_1": products['tools'],
    "stock_input_1": 0,
    "max_store_input_1": 1000,
    "input_2": products['pipe'],
    "stock_input_2": 0,
    "max_store_input_2": 1000,
    "input_3": products['beams'],
    "stock_input_3": 0,
    "max_store_input_3": 1000,
    "output_1": products['crude_oil'],
    "stock_output_1": 0,
    "max_store_output_1": 1000,
    "ratio": production_ratio['oil_well'],
}

oil_refinery = {
    "name": industries['Oil Refinery'],
    "map": asset_url['oil_refinery'],
    "input_1": products['crude_oil'],
    "stock_input_1": 0,
    "max_store_input_1": 1000,
    "input_2": products['lumber'],
    "stock_input_2": 0,
    "max_store_input_2": 1000,
    "input_3": products['pipe'],
    "stock_input_3": 0,
    "max_store_input_3": 1000,
    "output_1": products['oil_barrel'],
    "stock_output_1": 0,
    "max_store_output_1": 1000,
    "ratio": production_ratio['oil_refinery'],
}

freight_depot = {
    "name": yards['freight_depot'],
    "map": asset_url['freight_depot'],
    "input_1": products['logs'],
    "max_store_input_1": 1000,
    "input_2": products['cordwood'],
    "max_store_input_2": 1000,
    "input_3": products['lumber'],
    "max_store_input_3": 1000,
    "input_4": products['beams'],
    "max_store_input_4": 1000,
    "input_5": products['iron_ore'],
    "max_store_input_5": 1000,
    "input_6": products['raw_iron'],
    "max_store_input_6": 1000,
    "input_7": products['rails'],
    "max_store_input_7": 1000,
    "input_8": products['coal'],
    "max_store_input_8": 1000,
    "input_9": products['pipe'],
    "max_store_input_9": 1000,
    "input_10": products['tools'],
    "max_store_input_10": 1000,
    "input_11": products['crude_oil'],
    "max_store_input_11": 1000,
    "input_12": products['oil_barrel'],
    "max_store_input_12": 1000,
}

flatcar = {
    "name": cars['flatcar'],
    "type": type_rolling_stock['flatcar'],
    "durability": 100,
    "max_durability": 100,
    "durability_reduction": 1,
    "is_derailed": False,
    "is_out_of_service": False,
    "is_assigned_to_consist": False,
    "product_1": products['logs'],
    "max_load_1": 8,
    "product_2": products['pipe'],
    "max_load_2": 6,
}

stake_flatcar = {
    "name": cars['stake_flatcar'],
    "type": type_rolling_stock['stake_flatcar'],
    "durability": 100,
    "max_durability": 100,
    "durability_reduction": 1,
    "is_derailed": False,
    "is_out_of_service": False,
    "is_assigned_to_consist": False,
    "product_1": car_load['stake_flatcar']['load_1'][0],
    "max_load_1": car_load['stake_flatcar']['load_1'][1],
    "product_2": car_load['stake_flatcar']['load_2'][0],
    "max_load_2": car_load['stake_flatcar']['load_2'][1],
}

bulkhead_flatcar = {
    "name": cars['bulkhead_flatcar'],
    "type": type_rolling_stock['bulkhead_flatcar'],
    "durability": 100,
    "max_durability": 100,
    "durability_reduction": 1,
    "is_derailed": False,
    "is_out_of_service": False,
    "is_assigned_to_consist": False,
    "product_1": car_load['bulkhead_flatcar']['load_1'][0],
    "max_load_1": car_load['bulkhead_flatcar']['load_1'][1],
    "product_2": car_load['bulkhead_flatcar']['load_2'][0],
    "max_load_2": car_load['bulkhead_flatcar']['load_2'][1],
}

hopper_car = {
    "name": cars['hopper'],
    "type": type_rolling_stock['hopper'],
    "durability": 100,
    "max_durability": 100,
    "durability_reduction": 1,
    "is_derailed": False,
    "is_out_of_service": False,
    "is_assigned_to_consist": False,
    "product_1": car_load['hopper']['load_1'][0],
    "max_load_1": car_load['hopper']['load_1'][1],
    "product_2": car_load['hopper']['load_2'][0],
    "max_load_2": car_load['hopper']['load_2'][1],
}

tank_car = {
    "name": cars['tank_car'],
    "type": type_rolling_stock['tank_car'],
    "durability": 100,
    "max_durability": 100,
    "durability_reduction": 1,
    "is_derailed": False,
    "is_out_of_service": False,
    "is_assigned_to_consist": False,
    "product_1": car_load['tank_car']['load_1'][0],
    "max_load_1": car_load['tank_car']['load_1'][1],
}

boxcar = {
    "name": cars['boxcar'],
    "type": type_rolling_stock['boxcar'],
    "durability": 100,
    "max_durability": 100,
    "durability_reduction": 1,
    "is_derailed": False,
    "is_out_of_service": False,
    "is_assigned_to_consist": False,
    "product_1": car_load['boxcar']['load_1'][0],
    "max_load_1": car_load['boxcar']['load_2'][1],
}
""" Crew settings"""
crew_config = {
    'radio': ['train_radio', 'dispatch_radio', 'prio_speaker', 'crew_lounge', 'create_train_radio'],
    'timetable': ['view_timetable', 'delete_timetable', 'create_timetable', 'update_timetable'],
    'switch_list': ['create_switch_list', 'view_switch_list', 'update_switch_list', 'delete_switch_list'],
    'consist_table': ['create_consist_table', 'view_consist_table', 'update_consist_table', 'delete_consist_table'],
    'item_manager': ['create_item', 'view_item', 'update_item', 'delete_item', 'set_rail_flag',
                     'set_out_of_service_flag'],
    'load_unload': ['load_car', 'unload_car']
}


conductor_config = {
        'radio': {
            crew_config['radio'][0]: True,  # train radio
            crew_config['radio'][1]: True,  # dispatch radio
            crew_config['radio'][2]: False,  # prio speaker
            crew_config['radio'][3]: True,  # crew lounge
            crew_config['radio'][4]: True,  # create train radio
        },
        'timetable': {
            crew_config['timetable'][0]: True, #view timetable
            #crew_config['timetable'][1]: True, #delete timetable
            #crew_config['timetable'][2]: True, #create timetable
            #crew_config['timetable'][3]: True, #update timetable
        },
        'switch_list': {
            #crew_config['switch_list'][0]: True, #create switch list
            crew_config['switch_list'][1]: True, #view switch list
            crew_config['switch_list'][2]: True, #update switch list
            #crew_config['switch_list'][3]: True, #delete switch list

        },
        'consist_table': {
            crew_config['consist_table'][0]: True, #create consist table
            crew_config['consist_table'][1]: True, #view consist table
            crew_config['consist_table'][2]: True, #update consist table
            crew_config['consist_table'][3]: True, #delete consist table
        },
        'load_unload': {
            crew_config['load_unload'][0]: True,
            crew_config['load_unload'][1]: True,
        },
}




