from dataclasses import dataclass
from typing import Protocol
from location import Location


@dataclass
class RollingStock:
    name: str
    durability: int
    max_durability: int
    railroad: str | None = None
    road_number_prefix: str | None = None
    road_number: int | None = None
    location: Location | None = None
    last_service_date: str | None = None
    is_derailed: bool = False
    is_out_of_service: bool = False
    is_assigned_to_consist: bool = False


class RollingStockConfig(Protocol):

    def show_location(self) -> str:
        ...

    def show_durability(self) -> str:
        ...

    def show_road_number(self) -> str:
        ...

    def show_railroad(self) -> str:
        ...

    def set_location(self, location: str) -> None:
        ...

    def set_derailment(self) -> None:
        ...

    def set_durability(self, durability: int) -> None:
        ...

    def set_out_of_service(self) -> None:
        ...

    def reset_derailment(self) -> None:
        ...

    def reset_out_of_service(self) -> None:
        ...

    def assign_to_consist(self, consist_id: int) -> None:
        ...

    def clear_from_consist(self) -> None:
        ...

    def __str__(self) -> str:
        ...


@dataclass
class Car(RollingStock):
    product_1: str | None = None
    load_1: int = 0
    max_load_1: int = 0
    product_2: str | None = None
    load_2: int = 0
    max_load_2: int = 0


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

