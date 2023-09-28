from enum import StrEnum


class AssetUrl(StrEnum):
    """
    All the logs, documentation, maps and rulebook.
    Sets up all s3 endpoints

    """
    """Empty"""
    none = 'none'
    """Dispatcher Track Diagrams"""
    dispatcher_schematic_cn = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_cn.png'
    dispatcher_schematic_arr = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_arr.png'
    dispatcher_schematic_alc = 'https://railroad-dispatcher.s3.amazonaws.com/dispatcher_schematic_alc.png'
    """Track Diagrams per industry"""
    loging_camp = 'https://railroad-dispatcher.s3.amazonaws.com/logging_camp.png'
    sawmill = 'https://railroad-dispatcher.s3.amazonaws.com/sawmill.png'
    iron_mine = 'https://railroad-dispatcher.s3.amazonaws.com/iron_mine.png'
    smelter = 'https://railroad-dispatcher.s3.amazonaws.com/smelter.png'
    coal_mine = 'https://railroad-dispatcher.s3.amazonaws.com/coal_mine.png'
    steel_mill = 'https://railroad-dispatcher.s3.amazonaws.com/steel_mill.png'
    oil_well = 'https://railroad-dispatcher.s3.amazonaws.com/oil_well.png'
    oil_refinery = 'https://railroad-dispatcher.s3.amazonaws.com/oil_refinery.png'
    freight_depot = 'https://railroad-dispatcher.s3.amazonaws.com/freight_depot.png'
    """Track Diagrams per yard"""
    freight_depot_yard = 'https://railroad-dispatcher.s3.amazonaws.com/freight_depot_yard.png'
    oil_field_yard = 'https://railroad-dispatcher.s3.amazonaws.com/oil_field_yard.png'
    coal_mine_yard = 'https://railroad-dispatcher.s3.amazonaws.com/coal_mine_yard.png'
    iron_mine_yard = 'https://railroad-dispatcher.s3.amazonaws.com/iron_mine_yard.png'
    smelter_yard = 'https://railroad-dispatcher.s3.amazonaws.com/smelter_yard.png'
    mine_yard = 'https://railroad-dispatcher.s3.amazonaws.com/mine_junction.png'
    sawmill_yard = 'https://railroad-dispatcher.s3.amazonaws.com/sawmill_yard.png'
    lumber_camp_yard = 'https://railroad-dispatcher.s3.amazonaws.com/lumber_camp_yard.png'
    """Rulebooks"""
    cn_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/cn_rulebook.pdf'
    arr_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/arr_rulebook.pdf'
    alc_rulebook = 'https://railroad-dispatcher.s3.amazonaws.com/alc_rulebook.pdf'
    """Maps"""
    cn_map = 'https://railroad-dispatcher.s3.amazonaws.com/cn_map.png'
    arr_map = 'https://railroad-dispatcher.s3.amazonaws.com/arr_map.png'
    alc_map = 'https://railroad-dispatcher.s3.amazonaws.com/alc_map.png'
    """Logs"""
    operations_log = 'https://railroad-dispatcher.s3.amazonaws.com/app.log'
    db_log = 'https://railroad-dispatcher.s3.amazonaws.com/db.log'
    chat_log = 'https://railroad-dispatcher.s3.amazonaws.com/chat.log'
    status_log = 'https://railroad-dispatcher.s3.amazonaws.com/status.log'
