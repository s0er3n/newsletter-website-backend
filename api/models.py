import typing
import strawberry


@strawberry.type
class Days:
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool

@strawberry.input
class DaysInput:
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool

@strawberry.type
class Subreddit:
    subreddit_name: str
    icon_url: str

@strawberry.type
class Options:
    time: str 
    frequenzy: Days


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
    frequenzy: DaysInput

@strawberry.input
class BlockInput:
    subreddit: str
    flairs: typing.List[str]
    count: int
    upvote_ratio: float

@strawberry.input
class NewsletterChangeInput:
    id:str
    user_id: str
    options: OptionsInput
    blocks: typing.List[BlockInput]


@strawberry.input
class NewsletterInput:
    user_id: str
    options: OptionsInput
    blocks: typing.List[BlockInput]

@strawberry.type
class User:
    newsletter: typing.List[Newsletter]
