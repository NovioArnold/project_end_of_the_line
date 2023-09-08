from dataclasses import dataclass
from rollingstock import RollingStock


@dataclass
class Locomotive(RollingStock):
    type: str | None = None
    fuel: str | None = None
    wheel_arrangement: str | None = None
    class_engines: str | None = None
    fuel_type: str | None = None
    fuel_capacity: int = 0
    fuel_max_capacity: int = 0
    water_level: int = 0
    water_max_capacity: int = 0
    has_engineer: bool = False
    has_fireman: bool = False


