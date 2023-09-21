from pydantic import BaseModel, Field
from main.railroads.companies import Railroad
from main.location.location import Location


class Track(BaseModel):
    type: str
    length: int
    number: str
    is_occupied: bool
    is_in_service: bool
    is_routed: bool

    def __str__(self) -> str:
        return (self.type + '\n' + str(self.length) + '\n' + self.number + '\n' + str(self.is_occupied) + '\n' +
                str(self.is_in_service) + '\n' + str(self.is_routed))

    def set_occupation(self) -> bool | ValueError:
        if self.is_occupied:
            return ValueError(f'Track {self.number} already occupied')
        else:
            self.is_occupied = True
            return self.is_occupied

    def reset_occupation(self) -> bool | ValueError:
        if not self.is_occupied:
            return ValueError(f'Track {self.number} already unoccupied')
        else:
            self.is_occupied = False
            return self.is_occupied


class TrackSection(BaseModel):
    name: str
    railroad: Railroad.name
    location: Location.name
    tracks: list[Track] = Field(default_factory=list)

    def __str__(self) -> str:
        return self.name + '\n' + self.railroad + '\n' + self.location + '\n' + self.show_tracks()

    def show_tracks(self) -> str:
        return self.tracks.__str__()

