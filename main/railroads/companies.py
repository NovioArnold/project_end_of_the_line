from pydantic import BaseModel

class Railroad(BaseModel):
    name: str
    prefix: str
