from location import Location
from config import flatcar
from car import Car, CarConfig
from typing import List, Dict, Iterator, Protocol

car_table: Dict[str, Car] = {}


def create(railroad: str, prefix: str, number: int, location: Location) -> str:
    nc = Car(**flatcar)
    nc.railroad = railroad
    nc.road_number_prefix = prefix
    nc.road_number = number
    nc.location = location
    car_table[prefix+str(number)] = nc
    return f'car created {nc} '


def show_all() -> List[str]:
    flatcar_list: list[str] = []
    for car in car_table:
        print(car)
        flatcar_list.append(car)
    return flatcar_list


def show_by_roadnumber(road_number: int, prefix: str) -> str:
    r_num: str = prefix+str(road_number)
    if r_num in car_table:
        return r_num
    else:
        return f'car {r_num} not found'


def show_by_railroad(r_name: str) -> List[str]:
    railroad_list: List[str] = []
    for car in car_table:
        if car_table[car].railroad == r_name:
            railroad_list.append(car)
    return railroad_list


create('B&O','C&O', 1234, Location(name='Cumberland', map_url='MD'))
create('B&O','C&O', 5678, Location(name='Cumberland', map_url='MD'))

print(car_table['C&O1234'].road_number_prefix)
print(show_all())
print(show_by_railroad('B&O'))


