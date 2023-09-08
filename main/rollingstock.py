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







