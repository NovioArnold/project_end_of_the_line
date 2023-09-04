from dataclasses import dataclass
from typing import Protocol


@dataclass
class Location:
    name: str | None = None
    map: str | None = None


class DefaultLocationConfig(Protocol):
    def load_car(self, quantity: int, product: str) -> None:
        ...

    def unload_car(self, quantity: int, product: str) -> None:
        ...

    def show_stock(self) -> None:
        ...

    def __str__(self) -> str:
        ...

    def produce_output(self,  ratio: tuple) -> int | None:
        ...
