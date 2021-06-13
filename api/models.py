import typing
import strawberry



@strawberry.type
class Options:
    time: str 
    frequenzy: int


@strawberry.type
class Block:
    subreddit: str
    flairs: typing.List[str]
    count: int
    upvote_ratio: float


@strawberry.type
class Newsletter:
    id: str
    user_id: str
    options: Options
    blocks: typing.List[Block]


@strawberry.input
class OptionsInput:
    time: str
    frequenzy: int


@strawberry.input
class BlockInput:
    subreddit: str
    flairs: typing.List[str]
    count: int
    upvote_ratio: float


@strawberry.input
class NewsletterInput:
    user_id: str
    options: OptionsInput
    blocks: typing.List[BlockInput]

@strawberry.type
class User:
    newsletter: typing.List[Newsletter]
