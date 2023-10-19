
from main.config.variables import jobs
from main.config.users import (
    RadioRights,
    TimetableRights,
    SwitchListRights,
    ConsistTableRights,
    ItemManagerRights,
    LoadUnloadRights,
    FlagRights,
    EnumJobs
)
from dataclasses import dataclass, field


"""all the jobs on the railroad and their rights"""


@dataclass
class Rights:
    name: str = EnumJobs.no_role
    radio_rights: RadioRights = field(default_factory=RadioRights)
    timetable_rights: TimetableRights = field(default_factory=TimetableRights)
    switch_list_rights: SwitchListRights = field(default_factory=SwitchListRights)
    consist_table_rights: ConsistTableRights = field(default_factory=ConsistTableRights)
    item_manager_rights: ItemManagerRights = field(default_factory=ItemManagerRights)
    load_unload_rights: LoadUnloadRights = field(default_factory=LoadUnloadRights)
    flag_rights: FlagRights = field(default_factory=FlagRights)


    def __str__(self) -> str:
        return f'{self.name}'











