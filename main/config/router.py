from pydantic import BaseModel, Field

from tracks import Mainline, Siding, Junctions, Yards, TrackSection, TrackTypes, Route

from logger import logger


ROUTER = Route


class Router(BaseModel):
    """Router for the dispatcher"""
    route_name: ROUTER = Field(default=ROUTER.none, title='Route Name', type=str)
    consist_id: str = Field(default='', title='Consist ID')
    track_section: list[Mainline] = Field(default_factory=list, default=Mainline.none, title='Track Section')

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

    def add_track_section(self, track_section: Mainline) -> list[Mainline] | ValueError:
        """add track section to route"""
        try:
            #  try to add section to route
            self.track_section.append(Mainline(track_section))
            logger.info(f'{track_section} added to route')
            return self.track_section
        except ValueError as e:
            logger.error(f' {e} is not a valid track section')
            return e

    def remove_track_section(self, track_section: Mainline) -> list[Mainline] | ValueError:
        """remove track section from route"""
        try:
            #  try to remove section from route
            self.track_section.remove(Mainline(track_section))
            logger.info(f'{track_section} removed from route')
            return self.track_section
        except ValueError as e:
            logger.error(f' {e} is not a valid track section')
            return e

