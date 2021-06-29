from __future__ import annotations
from functools import lru_cache
import os
from dataclasses import asdict
from api.models import NewsletterInput, Newsletter, NewsletterChangeInput, Subreddit
from api.mongodb import get_newsletters, create_newsletter, delete_newsletter, change_newsletter
import uuid
import typing
import strawberry
import asyncpraw
from dotenv import load_dotenv
load_dotenv()
reddit = asyncpraw.Reddit(
    client_id=os.environ.get("client_id"),
    client_secret=os.environ.get("client_secret"),
    password=os.environ.get("password"),
    user_agent=os.environ.get("user_agent"),
    username=os.environ.get("username")
)

cache = {}
async def get_subreddit_icon_link(self, subredditnamelist: typing.List[str]) -> typing.List[Subreddit]:
    iconsDict = []
    for subredditname in subredditnamelist:
        if subredditname not in cache:
            subreddit = await reddit.subreddit(subredditname)
            await subreddit.load()
            icon = subreddit.icon_img if subreddit.icon_img else subreddit.community_icon
            cache[subredditname] = icon
            iconsDict.append(  Subreddit(subredditname,  icon))
            continue
        iconsDict.append(Subreddit(subredditname,cache[subredditname]))
    return iconsDict

@strawberry.type
class Query:
    @strawberry.field
    def fetch_newsletters(self,user_id: str, newsletter_id:str= None) -> typing.List[Newsletter]:
        return get_newsletters(user_id, newsletter_id)

    get_subreddit_icon_link: typing.List[Subreddit] = strawberry.field(resolver=get_subreddit_icon_link)


@strawberry.type
class Mutation:


    @strawberry.mutation
    def make_newsletter(self, newsletter: NewsletterInput) -> str:
        return create_newsletter(newsletter)

    @strawberry.mutation
    def remove_newsletter(self, newsletter_id:str) -> str:
        return delete_newsletter(newsletter_id)


    @strawberry.mutation
    def update_newsletter(self, id: str, newsletter: NewsletterChangeInput) -> str:
        return change_newsletter(id, newsletter)

schema = strawberry.Schema(query=Query, mutation=Mutation)

