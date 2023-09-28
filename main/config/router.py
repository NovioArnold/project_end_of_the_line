from pydantic import BaseModel, Field

from tracks import Mainline, Siding, Junctions, Yards, TrackSection, TrackTypes, Route
from location import Location

from logger import logger


ROUTER = Route
MAINLINE = Mainline
SIDING = Siding
JUNCTIONS = Junctions
YARDS = Yards
TRACK_SECTION = TrackSection
TRACK_TYPES = TrackTypes
LOCATION = Location


class Router(BaseModel):
    """Router for the dispatcher"""
    route_name: ROUTER = Field(default=ROUTER.none, title='Route Name', type=str)
    consist_id: str = Field(default='', title='Consist ID')
    track_section: list[MAINLINE] = Field(default_factory=list, default=MAINLINE.none, title='Track Section')

    def __str__(self):
        return f'{self.route_name} {self.track_section.__str__()}'

    def name_route(self, route_name: str) -> route_name | ValueError:
        """see if route name is valid"""
        try:
            self.route_name = ROUTER(route_name)
            logger.info(f'route name is {self.route_name} is set')
            return self.route_name
        except ValueError as e:
            logger.error(f' {e} is not a valid route name')
            return e

    def add_track_section(self, track_section: str) -> list[MAINLINE] | ValueError:
        try:
            #  try to add section to route
            self.track_section.append(MAINLINE(track_section))
            logger.info(f'{track_section} added to route')
            return self.track_section
        except ValueError as e:
            logger.error(f' {e} is not a valid track section')
            return e

    def remove_track_section(self, track_section: str) -> list[MAINLINE] | ValueError:
        """remove track section from route"""
        try:
            #  try to remove section from route
            self.track_section.remove(MAINLINE(track_section))
            logger.info(f'{track_section} removed from route')
            return self.track_section
        except ValueError as e:
            logger.error(f' {e} is not a valid track section')
            return e

    def clear_route(self) -> list[Mainline]:
        """clear route"""
        self.track_section.clear()
        logger.info(f'route cleared')
        return self.track_section

    def get_route(self) -> list[Mainline]:
        """get route"""
        logger.info(f'route {self.track_section} returned')
        return self.track_section

    def get_route_name(self) -> str:
        """get route name"""
        logger.info(f'route name {self.route_name} returned')
        return self.route_name

    def get_consist_id(self) -> str:
        """get consist id"""
        logger.info(f'consist id {self.consist_id} returned')
        return self.consist_id


class SetUpTrackSection(BaseModel):
    section_name: TRACK_SECTION = Field(default=TRACK_SECTION.none, title='Section Name', type=str)
    location: LOCATION = Field(default=LOCATION.name, title='Location', type=str)
    track_type: TRACK_TYPES = Field(default=TRACK_TYPES.none, title='Track Type', type=str)
    track_length: int = Field(default=0, title='Track Length', type=int)






