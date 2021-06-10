import typing
import strawberry
import datetime

@strawberry.type
class Options:
    time: datetime.time
    frequenzy: int


@strawberry.type
class Block:
    subreddit: str
    flairs: typing.List[str]
    count: int
    upvote_ratio: float


@strawberry.type
class Newsletter:
    user_id: strawberry.ID
    options: Options
    blocks: typing.List[Block]


@strawberry.input
class OptionsInput:
    time: datetime.time
    frequenzy: int


@strawberry.input
class BlockInput:
    subreddit: str
    flairs: typing.List[str]
    count: int
    upvote_ratio: float


@strawberry.input
class NewsletterInput:
    user_id: strawberry.ID
    options: OptionsInput
    blocks: typing.List[BlockInput]
