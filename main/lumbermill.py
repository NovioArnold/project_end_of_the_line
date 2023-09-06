from industry import Industry
from config import sawmill, production_ratio
from location import DefaultLocationConfig
from helper import product_from_self, product_to_self


class LumberMillConfig(DefaultLocationConfig):
    lm: Industry = Industry(**sawmill)
    name: str = lm.name
    map: str = lm.map
    input_1: str = lm.input_1
    stock_input_1: int = lm.stock_input_1
    max_store_input_1: int = lm.max_store_input_1
    output_1: str = lm.output_1
    output_2: str = lm.output_2
    stock_output_1: int = lm.stock_output_1
    stock_output_2: int = lm.stock_output_2
    max_store_output_1: int = lm.max_store_output_1
    max_store_output_2: int = lm.max_store_output_2
    ratio: tuple = lm.ratio

    def unload_car(self, quantity: int, product: str) -> None:
        if product == self.input_1:
            print(self.input_1)
            self.stock_input_1 = product_to_self(
                stock=self.stock_input_1,
                quantity=quantity,
                max_store=self.max_store_input_1
            )
        else:
            raise ValueError(f'cannot unload {product} at {self.name}')

    def load_car(self, quantity: int, product: str) -> None:
        # TODO: Add car loading logic when that is implemented

        if product == self.output_1:
            self.stock_output_1 = product_from_self(
                stock=self.stock_output_1,
                quantity=quantity
            )

        elif product == self.output_2:
            self.stock_output_2 = product_from_self(
                stock=self.stock_output_2,
                quantity=quantity,
            )
        else:
            raise ValueError(f'Product {product} not found')

    def produce_output(self, ratio: tuple) -> None:
        while self.stock_input_1 >= ratio[0]:  # check if there is enough input to produce
            # check if there is enough space in the storage to store the output
            if (self.stock_output_1 + ratio[1]/2 <= self.max_store_output_1
                    and self.stock_output_2 + ratio[1]/2 <= self.max_store_output_2):
                # Produces both outputs
                self.stock_input_1 -= ratio[0]
                self.stock_output_1 += ratio[1]/2
                self.stock_output_2 += ratio[1]/2
            elif self.stock_output_1 + ratio[1] <= self.max_store_output_1:
                # Produces only output 1 cause output 2 is full
                self.stock_input_1 -= ratio[0]
                self.stock_output_1 += ratio[1]
            elif self.stock_output_2 + ratio[1] <= self.max_store_output_2:
                # Produces only output 2 cause output 1 is full
                self.stock_input_1 -= ratio[0]
                self.stock_output_2 += ratio[1]
            else:
                print('storage full no production possible')
        else:
            print(f'not enough input {self.input_1} to produce')

    def __str__(self) -> str:
        return f'{self.name} = {self.output_1} : {self.stock_output_1}/{self.max_store_output_1} ,{self.output_2} : {self.stock_output_2}/{self.max_store_output_2}'

    def show_stock(self) -> None:
        print(self.__str__())
