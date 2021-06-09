import typing
import strawberry
from dataclasses import asdict

@strawberry.type
class Options:
    time: str
    frequenzy: str


@strawberry.type
class Block:
    subreddit: str
    flairs: typing.List[str]
    count: int
    upvote_ratio: float


@strawberry.type
class Newsletter:
    user_id: str
    options: Options
    blocks: typing.List[Block]
