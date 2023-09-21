from pydantic import BaseModel


class Location(BaseModel):
    name: str
    map_url: str

    def __str__(self) -> str:
        return self.name + '\n' + self.map_url
