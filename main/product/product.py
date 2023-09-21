from pydantic import BaseModel, Field
from main.helper import eval_int, greater_int


class Product(BaseModel):
    name: str
    in_stock: int
    max_store: int

    def __str__(self) -> str:
        return self.name + '\n' + str(self.in_stock) + '\n' + str(self.max_store)

    def add_stock(self, quantity: int) -> int | ValueError:
        if eval_int(self.in_stock, self.max_store):
            return ValueError(f'Product {self.name} already has max stock')
        elif greater_int(self.in_stock + quantity, self.max_store):
            self.in_stock = self.max_store
            return self.in_stock
        else:
            self.in_stock += quantity
            return self.in_stock



