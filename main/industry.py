from dataclasses import dataclass
from typing import Optional

from main.location.location import Location
from main.config.industries import IndustryConfig




@dataclass
class Industry:
    name: str
    location: Location
    config: IndustryConfig

    def load_input(self, product: str, quantity: int) -> int:
        if product == self.config.input_1:
            self.config.stock_input_1 += quantity
            return self.config.stock_input_1
        elif product == self.config.input_2:
            self.config.stock_input_2 += quantity
            return self.config.stock_input_2
        elif product == self.config.input_3:
            self.config.stock_input_3 += quantity
            return self.config.stock_input_3
        else:
            return 0

    def unload_input(self, product: str, quantity: int) -> int:
        if product == self.config.input_1:
            self.config.stock_input_1 -= quantity
            return self.config.stock_input_1
        elif product == self.config.input_2:
            self.config.stock_input_2 -= quantity
            return self.config.stock_input_2
        elif product == self.config.input_3:
            self.config.stock_input_3 -= quantity
            return self.config.stock_input_3
        else:
            return 0
























