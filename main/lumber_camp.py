from time import sleep
from industry import Industry
from config import loging_camp
from location import DefaultLocationConfig
from helper import product_from_self


class LumberCampConfig(DefaultLocationConfig):
    lc: Industry = Industry(**loging_camp)
    name: str = lc.name
    map: str = lc.map
    output_1: str = lc.output_1
    output_2: str = lc.output_2
    stock_output_1: int = lc.stock_output_1
    stock_output_2: int = lc.stock_output_2
    max_store_output_1: int = lc.max_store_output_1
    max_store_output_2: int = lc.max_store_output_2

    def unload_car(self, quantity: int, product: str) -> None:
        raise NotImplementedError(f'This industry {self.name} does not unload cars')

    def produce_output(self, ratio: tuple) -> None:
        raise NotImplementedError(f'This industry {self.name} does not have a recipe')

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

    def reset_stock(self, sec: float = 2400.0) -> None:
        self.show_stock()
        sleep(sec)
        print("Resetting stock")
        self.stock_output_1 = 100
        self.stock_output_2 = 100

    def __str__(self) -> str:
        return (f'{self.name} = {self.output_1} : {self.stock_output_1}/{self.max_store_output_1} '
                f',{self.output_2} : {self.stock_output_2}/{self.max_store_output_2}')

    def show_stock(self) -> None:
        print(self.__str__())
