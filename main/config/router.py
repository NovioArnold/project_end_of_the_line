from dataclasses import dataclass, field

from main.config.location import Location
from main.config.logger import logger
from main.config.tracks import (
    Junctions,
    Mainline,
    Route,
    Siding,
    TrackSection,
    TrackTypes,
    Yards,
)


@dataclass
class Router:
    """Router for the dispatcher"""

    consist_id: str = "none"
    route_name: Route = Route.none
    track_section: list[Mainline] = field(default_factory=list)

    def __str__(self):
        return f"{self.route_name} {self.track_section.__str__()}"

    def get_route(self) -> list[Mainline]:
        """get route"""
        logger.info(f"route {self.track_section} returned")
        return self.track_section

    def get_route_name(self) -> str:
        """get route name"""
        logger.info(f"route name {self.route_name} returned")
        return self.route_name

    def get_consist_id(self) -> str:
        """get consist id"""
        logger.info(f"consist id {self.consist_id} returned")
        return self.consist_id


@dataclass
class SetUpTrackSection:
    """sets up the track sections"""

    section_name: TrackSection = TrackSection.none
    location: Location = field(default_factory=Location)
    track_type: TrackTypes = TrackTypes.none
    track_length: int = 0

    def __str__(self) -> str:
        """string output for the track_section"""
        return f"{self.section_name} is located at {self.location} and is a {self.track_type} and holds a max of {self.track_length} rollingstock"
