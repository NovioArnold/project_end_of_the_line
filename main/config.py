# Desc: Configuration file for project buffer


products = {
    0: 'Logs',
    1: 'Cordwood',
    2: "Lumber",
    3: "Beams",
    4: "Iron Ore",
    5: "Raw Iron",
    6: "Rails",
    7: "Coal",
    8: "Pipe",
    9: "Tools",
    10: "Crude Oil",
    11: "Barrel oil",
}

industries = {
    0: "Logging Camp",
    1: "Sawmill",
    2: "Iron Mine",
    3: "Smelter",
    4: "Coal Mine",
    5: "Steel Mill",
    6: "Oil Well",
    7: "Oil Refinery",
    8: "Freight Depot",
}

cars = {
    0: "flatcar",
    1: "stakecar",
    2: "headerflatcar",
    3: "hopper",
    4: "tanklcar",
    5: "boxcar",
    6: "caboose",
}

engine = {
    0: 'porter-0-4-0',
}

loging_camp = {
    "name": "Loging Camp",
    "map": "map",
    "input_1": None,
    "stock_input_1": 0,
    "max_store_input_1": 0,
    "input_2": None,
    "stock_input_2": 0,
    "max_store_input_2": 0,
    "input_3": None,
    "in_stock_input_3": 0,
    "max_store_input_3": 0,
    "output_1": "Logs",
    "stock_output_1": 100,
    "max_store_output_1": 100,
    "output_2": 'Cordwood',
    "stock_output_2": 100,
    "max_store_output_2": 100,

}

sawmill = {
    "name": "Sawmill",
    "map": "Sawmill",
    "input_1": "Logs",
    "stock_input_1": 0,
    "max_store_input_1": 100,
    "input_2": None,
    "stock_input_2": 0,
    "max_store_input_2": 0,
    "input_3": None,
    "in_stock_input_3": 0,
    "max_store_input_3": 0,
    "output_1": "Lumber",
    "stock_output_1": 0,
    "max_store_output_1": 100,
    "output_2": 'Beams',
    "stock_output_2": 0,
    "max_store_output_2": 100,

}
production_ratio = {
     "sawmill": {
            "input": 2,
            "output": 2,
     },
 }

