from pydantic import BaseModel
from pydantic import BaseModel
from typing import List
from .blocks import Block


class Newsletter(BaseModel):
    id: str
    share_code: str
    period: str
    time: str
    blocks: List[Block]

    class IN(BaseModel):
        period: str
        time: str
        blocks: List[Block]
