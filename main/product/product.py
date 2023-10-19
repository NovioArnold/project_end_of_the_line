from pydantic import BaseModel

from main.helper import eval_int, greater_int


class Product(BaseModel):
    """this is the product base class"""

    name: str
    in_stock: int
    max_store: int

    def __str__(self) -> str:
        return self.name + "\n" + str(self.in_stock) + "\n" + str(self.max_store)

    def add_stock(self, quantity: int) -> int | ValueError:
        """to add stock to storrage upto max_store limit"""
        if eval_int(self.in_stock, self.max_store):
            return ValueError(f"Product {self.name} already has max stock")
        if greater_int(self.in_stock + quantity, self.max_store):
            self.in_stock = self.max_store
            return self.in_stock
        self.in_stock += quantity
        return self.in_stock

    def remove_stock(self, quantity: int) -> int | ValueError:
        """remove quantity from stock, cannot be lower than 0"""
        if self.in_stock == 0:
            return ValueError(f"stock is {self.in_stock}")
        if self.in_stock - quantity < 0:
            return ValueError(f"stock {self.stock} is lower than {quantity}")
        self.in_stock -= quantity
        return self.in_stock

    def view_stock(self) -> int:
        """view the quantity in stock"""
        return self.in_stock
