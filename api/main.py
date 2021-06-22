from __future__ import annotations
from functools import lru_cache
from dataclasses import asdict
from api.models import NewsletterInput, Newsletter, NewsletterChangeInput
from api.mongodb import get_newsletters, create_newsletter, delete_newsletter, change_newsletter
import uuid
import typing
import strawberry
import praw
from dotenv import load_dotenv
load_dotenv()
reddit = praw.Reddit(
    client_id=os.environ.get("client_id"),
    client_secret=os.environ.get("client_secret"),
    password=os.environ.get("password"),
    user_agent=os.environ.get("user_agent"),
    username=os.environ.get("username")
)




@strawberry.type
class Query:
    @strawberry.field
    def fetch_newsletters(self,user_id: str, newsletter_id:str= None) -> typing.List[Newsletter]:
        return get_newsletters(user_id, newsletter_id)

    @lru_cache(maxsize=128)
    @strawberry.field
    def get_subreddit_icon_link(self, subreddit: str) -> str:
        return reddit.subreddit(subreddit).icon_img



@strawberry.type
class Mutation:


    def make_newsletter(self, newsletter: NewsletterInput) -> str:
        return create_newsletter(newsletter)

    @strawberry.mutation
    def remove_newsletter(self, newsletter_id:str) -> str:
        return delete_newsletter(newsletter_id)


    @strawberry.mutation
    def update_newsletter(self, id: str, newsletter: NewsletterChangeInput) -> str:
        return change_newsletter(id, newsletter)

schema = strawberry.Schema(query=Query, mutation=Mutation)

