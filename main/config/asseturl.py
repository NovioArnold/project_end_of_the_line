from enum import StrEnum


class AssetUrl(StrEnum):
    """
    All the logs, documentation, maps and rulebook.
    Sets up all s3 endpoints

    """
    dispatcher_schematic_cn = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_cn.png'
    dispatcher_schematic_arr = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_arr.png'
    dispatcher_schematic_alc = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_alc.png'
    loging_camp = 'https://railroad-dispatcher.s3.amazonaws.com/logging_camp.png'
    sawmill = 'https://railroad-dispatcher.s3.amazonaws.com/sawmill.png'
    iron_mine = 'https://railroad-dispatcher.s3.amazonaws.com/iron_mine.png'
    smelter = 'https://railroad-dispatcher.s3.amazonaws.com/smelter.png'
    coal_mine = 'https://railroad-dispatcher.s3.amazonaws.com/coal_mine.png'
    steel_mill = 'https://railroad-dispatcher.s3.amazonaws.com/steel_mill.png'
    oil_well = 'https://railroad-dispatcher.s3.amazonaws.com/oil_well.png'
    oil_refinery = 'https://railroad-dispatcher.s3.amazonaws.com/oil_refinery.png'
    freight_depot = 'https://railroad-dispatcher.s3.amazonaws.com/freight_depot.png'
    # rulebooks
    cn_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/cn_rulebook.pdf'
    arr_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/arr_rulebook.pdf'
    alc_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/alc_rulebook.pdf'
    # maps
    cn_map = 'https://railroad-dispatcher.s3.amazonaws.com/cn_map.png'
    arr_map = 'https://railroad-dispatcher.s3.amazonaws.com/arr_map.png'
    alc_map = 'https://railroad-dispatcher.s3.amazonaws.com/alc_map.png'
    # logs
    operations_log = 'https://railroad-dispatcher.s3.amazonaws.com/operations_log.csv'
    db_log = 'https://railroad-dispatcher.s3.amazonaws.com/db_log.csv'
    chat_log = 'https://railroad-dispatcher.s3.amazonaws.com/chat_log.csv'
    status_log = 'https://railroad-dispatcher.s3.amazonaws.com/status_log.csv'
