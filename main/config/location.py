from pydantic import BaseModel, Field

from variables import railroads
from asseturl import AssetUrl

ASSETURL = AssetUrl
RAILROADS = railroads


class Location(BaseModel):
    """Locations on the railroad"""
    name: str = Field(default='none', title='Location Name', type=str)
    track_diagram: ASSETURL = Field(default=ASSETURL.none, title='Map', type=str)
    owner: dict[RAILROADS] = Field(default=RAILROADS[0], title='Owner', type=dict)

    def __str__(self) -> str:
        return f'{self.name} is owned by {self.owner["name"]}'

    def get_name(self) -> str:
        return self.name

    def get_owner(self) -> str:
        return self.owner["name"]

    def get_track_diagram_url(self) -> str:
        await self.track_diagram.value

