from dataclasses import dataclass
from rollingstock import RollingStock, RollingStockConfig
from location import Location


@dataclass
class Car(RollingStock):
    product_1: str | None = None
    load_1: int = 0
    max_load_1: int = 0
    product_2: str | None = None
    load_2: int = 0
    max_load_2: int = 0


class CarConfig(RollingStockConfig):
    name: str
    road_number_prefix: str
    road_number: int
    railroad: str
    durability: int
    max_durability: int
    is_derailed: bool
    is_out_of_service: bool
    is_assigned_to_consist: bool
    location: Location
    product_1: str
    load_1: int
    max_load_1: int
    product_2: str
    load_2: int
    max_load_2: int

    def show_location(self) -> str:
        return self.location.name

    def set_location(self, location: str) -> None:
        self.location.name = location

    def show_durability(self) -> str:
        return f'{self.durability}/{self.max_durability}'

    def reduce_durability(self, amount: int) -> None:
        self.durability -= amount

    def show_road_number(self) -> str:
        return f'{self.road_number_prefix} + {self.road_number}'

    def show_railroad(self) -> str:
        return self.railroad

    def show_load(self) -> str:
        if self.load_1 > 0:
            return f'{self.product_1} : {self.load_1}/{self.max_load_1}'
        elif self.load_2 > 0:
            return f'{self.product_2} : {self.load_2}/{self.max_load_2}'
        else:
            return 'Empty'



