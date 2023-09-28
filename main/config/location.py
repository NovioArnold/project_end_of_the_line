from pydantic import BaseModel, Field

from variables import railroads
from asseturl import AssetUrl

from logger import logger

ASSETURL = AssetUrl


class Railroad(BaseModel):
    name: str
    road_number_prefix: str


none = Railroad(name='None', road_number_prefix='none')
cn = Railroad(name='Canadian National', road_number_prefix='CN')
arr = Railroad(name='Alaska Railroad', road_number_prefix='ARR')
alc = Railroad(name='Arnold Lumber Company', road_number_prefix='ALC')
RAILROADS = [none, cn, arr, alc]

print(cn)


class Location(BaseModel):
    """Locations on the railroad"""
    name: str = Field(default='none')
    track_diagram: ASSETURL = Field(default=ASSETURL.none)
    owner: RAILROADS = Field(default=RAILROADS[0])

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
            self.owner['name'] = RAILROADS.name[owner]
            logger.info(f'{owner} added to location')
            return self.owner["name"]
        except ValueError as e:
            logger.error(f' {e} is not a valid railroad')
            return e


