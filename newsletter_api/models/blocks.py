from pydantic import BaseModel


class Block(BaseModel):
    type: str
    data: str
