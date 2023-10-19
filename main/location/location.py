from dataclasses import dataclass
from main.config.variables import location


@dataclass
class Location:
    map_url: str
    name: location = location[0]


    def __str__(self) -> str:
        return self.name + '\n' + self.map_url
