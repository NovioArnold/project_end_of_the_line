from typing import Optional
from pydantic import BaseModel, Field
from ..railroads.companies import Railroad
from main.helper import eval_bool, eval_int, eval_str
from ..product.product import Product
from main.location.location import Location
from main.tracks.tracks import Track, TrackSection
from main.crew.jobs import User


class Rollingstock(BaseModel):
    name: str
    company: Railroad.name
    prefix: Railroad.prefix
    location: Location.name
    track_section: TrackSection.name
    track: Track.number
    number: int
    durability: int
    max_durability: int
    reduce_durability: int
    id_assigned_to_consist: bool
    is_in_service: bool
    is_derailed: bool

    def __str__(self) -> str:
        return (self.name + '\n' + self.company + '\n' + self.prefix + '\n' + str(self.number) + '\n'
                + str(self.durability) + '\n' + str(self.max_durability) + '\n' + str(self.reduce_durability) + '\n' +
                str(self.id_assigned_to_consist) + '\n' + str(self.is_in_service) + '\n' + str(self.is_derailed))

    def change_durability(self, durability: int) -> int | ValueError:
        self.durability = durability
        return self.durability

    def reset_durability(self) -> int:
        self.durability = self.max_durability
        return self.durability

    def reduce_durability(self) -> int | ValueError:
        if eval_int(self.durability, 0):
            return ValueError(f'Rollingstock {self.name} already has 0 durability')
        else:
            self.durability -= self.reduce_durability
            return self.durability

    def assign_to_consist(self) -> bool | ValueError:
        if eval_bool(self.id_assigned_to_consist, False):
            self.id_assigned_to_consist = True
            return self.id_assigned_to_consist
        else:
            return ValueError(f'Rollingstock {self.name} already assigned to consist')

    def remove_from_consist(self) -> bool | ValueError:
        if eval_bool(self.id_assigned_to_consist, True):
            self.id_assigned_to_consist = False
            return self.id_assigned_to_consist
        else:
            return ValueError(f'Rollingstock {self.name} not a member of a consist')

    def is_derailed(self) -> bool | ValueError:
        if eval_bool(self.is_derailed, True):
            return ValueError(f'Rollingstock {self.name} already derailed')
        else:
            self.is_derailed = True
            return self.is_derailed

    def is_not_derailed(self) -> bool | ValueError:
        if eval_bool(self.is_derailed, False):
            return ValueError(f'Rollingstock {self.name} already on the tracks')
        else:
            self.is_derailed = False
            return self.is_derailed

    def is_in_service(self) -> bool | ValueError:
        if eval_bool(self.is_in_service, True):
            return ValueError(f'Rollingstock {self.name} already in service')
        else:
            self.is_in_service = True
            return self.is_in_service

    def is_not_in_service(self) -> bool | ValueError:
        if eval_bool(self.is_in_service, False):
            return ValueError(f'Rollingstock {self.name} already out of service')
        else:
            self.is_in_service = False
            return self.is_in_service


class Car(Rollingstock):
    type: str
    can_load: list[Product.name] = Field(default_factory=list)
    load_1: Optional[Product] = None

    def __str__(self) -> str:
        return (self.name + '\n' + self.company + '\n' + self.prefix + '\n' + str(self.number) + '\n'
                + str(self.durability) + '\n' + str(self.max_durability) + '\n' + str(self.reduce_durability) + '\n' +
                str(self.id_assigned_to_consist) + '\n' + str(self.is_in_service) + '\n' + str(self.is_derailed) +
                '\n' + self.type + '\n' + self.can_load.__str__() + '\n' + self.load_1.__str__())

    def load_product(self, product: str, load: int) -> Product.name | ValueError:
        if self.load_1.name is None and self.can_load.__contains__(product):
            self.load_1.name = product
            self.load_1.add_stock(quantity=load)
            return self.product_loaded, self.loaded
        else:
            return ValueError(f'Car {self.name} already loaded with {self.product_loaded}')

    def unload_product(self, product: str, unload: int) -> Product.name | ValueError:
        if self.load_1.name == product:
            self.load_1.remove_stock(quantity=unload)
            return self.product_loaded, self.loaded
        else:
            return ValueError(f'Car {self.name} not loaded with {self.product_loaded}')


class Engine(Rollingstock):
    type: str
    wheel_base: str
    fuel: Product = Field(default_factory=dict)
    water: Product = Field(default_factory=dict)
    sand: Product = Field(default_factory=dict)
    engineer: User.name
    fireman: User.name

    def __str__(self):
        return (super.__str__(self) + '\n' + self.type + "\n" + self.wheel_base + '/n' + self.fuel.__str__() +
                self.water.__str__() + '\n' + self.sand.__str__() + '\n' + self.enineer + '\n' + self.fireman)

    def load_product(self, product: str, quantity: int) -> Product | ValueError:
        if self.fuel.name == product:
            self.fuel.add_stock(quantity=quantity)
            return self.fuel
        elif self.water.name == product:
            self.water.add_stock(quantity=quantity)
            return self.water
        elif self.sand.name == product:
            self.sand.add_stock(quantity=quantity)
            return self.sand
        else:
            return ValueError(f'product {product} not compatible with this engine')

    def unload_product(self, product: str, quantity: int) -> Product | ValueError:
        if self.fuel.name == product:
            self.fuel.remove_stock(quantity=quantity)
            return self.fuel
        elif self.water.name == product:
            self.water.remove_stock(quantity=quantity)
            return self.water
        elif self.sand.name == product:
            self.sand.remove_stock(quantity=quantity)
            return self.sand
        else:
            return ValueError(f'product {product} not compatible with this engine')

    def add_product_new(self, product: str, quantity: int) -> Product | ValueError:
        match self.fuel:
            case 'fuel':
                self.fuel.add_stock(quantity=quantity)
                return self.fuel
            case 'water':
                self.water.add_stock(quantity=quantity)
                return self.water
            case 'sand':
                self.sand.add_stock(quantity=quantity)
                return self.sand
            case _:
                return ValueError(f'product {product} not compatible with this engine')



