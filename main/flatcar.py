from location import Location
from config import flatcar
from rollingstock import RollingStockConfig, Car


class FlatcarConfig(RollingStockConfig):
    fc: Car = Car(**flatcar)
    name: str = fc.name
    road_number_prefix: str = fc.road_number_prefix
    road_number: str = fc.road_number
    railroad: str = fc.railroad
    durability: int = fc.durability
    max_durability: int = fc.max_durability
    is_derailed: bool = fc.is_derailed
    is_out_of_service: bool = fc.is_out_of_service
    is_assigned_to_consist: bool = fc.is_assigned_to_consist
    location: Location = fc.location
    product_1: str = fc.product_1
    load_1: int = fc.load_1
    max_load_1: int = fc.max_load_1
    product_2: str = fc.product_2
    load_2: int = fc.load_2
    max_load_2: int = fc.max_load_2

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


