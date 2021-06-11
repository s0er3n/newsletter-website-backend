from __future__ import annotations
from dataclasses import asdict
from api.models import NewsletterInput, User, Newsletter
from api.mongodb import get_newsletters, create_newsletter, delete_newsletter
import uuid
import typing
import strawberry




@strawberry.type
class Query:
    @strawberry.field
    def fetch_newsletters(self,user_id: str, newsletter_id:str= None) -> typing.List[Newsletter] or str:
        return get_newsletters(user_id, newsletter_id)


@strawberry.type
class Mutation:

    # newsletter: str = strawberry.field(resolver=create_newsletter)
    #     @strawberry.mutation
    #     def create_user(self, id: str) -> bool:
    #         db["users"].append(User(id=id, newsletter=[]))
    #         return True

    @strawberry.mutation
    def make_newsletter(self, newsletter: NewsletterInput) -> str:
        print(newsletter)

        return create_newsletter(newsletter)

#     @strawberry.mutation
#     def create_block(self, newsletterid: str, subreddit: str, flairs: typing.List[str], count: int, upvote_ratio: float) -> bool:

#         for newsletter in db["newsletter"]:
#             if newsletter.id == newsletterid:
#                 id = str(uuid.uuid4())
#                 block = Block(id=id, subreddit=subreddit, flairs=flairs,
#                               count=count, upvote_ratio=upvote_ratio)
#                 newsletter.blocks.append(block)
#                 db["blocks"].append(block)
#                 return True
#         return False


schema = strawberry.Schema(query=Query, mutation=Mutation)

