
from dataclasses import dataclass, field

from main.config.variables import railroads, location
from main.config.asseturl import AssetUrl

from main.config.logger import logger



@dataclass
class Railroad:
    name: str
    road_number_prefix: str




@dataclass
class Location:
    """Locations on the railroad"""
    name: location = location[0]
    track_diagram: AssetUrl = AssetUrl.none
    owner: railroads = railroads[0]['name']

    def __str__(self) -> str:
        logger.info(f'{self.name} is owned by {self.owner["name"]}')
        return f'{self.name} is owned by {self.owner["name"]}'

    def get_name(self) -> str:
        logger.info(f'{self.name} returned')
        return self.name

    def get_owner(self) -> str:
        logger.info(f'{self.owner["name"]} returned')
        return self.owner["name"]

    def get_track_diagram_url(self) -> str:
        logger.info(f'{self.track_diagram} returned')
        return self.track_diagram

    def update_track_diagram_url(self, track_diagram_url: str) -> str | ValueError:
        try:
            self.track_diagram = ASSETURL(track_diagram_url)
            logger.info(f'{track_diagram_url} added to location')
            return self.track_diagram
        except ValueError as e:
            logger.error(f' {e} is not a valid track diagram url')
            return e

    def update_owner(self, owner: str) -> str | ValueError:
        try:
            self.owner['name'] = RAILROADS['name']
            logger.info(f'{owner} added to location')
            return self.owner["name"]
        except ValueError as e:
            logger.error(f' {e} is not a valid railroad')
            return e


