from __future__ import annotations
import uuid

import typing
import strawberry

db = {
        "newsletter" : [],
        "block" : [],
        "users" : []
        }

@strawberry.type
class Block:
    id: str
    subreddit: str
    flairs : typing.List[str]
    count: int
    upvote_ratio : float 


@strawberry.type
class User:
    id: str
    newsletter: typing.List[Newsletter]

@strawberry.type
class Newsletter:
    id: str
    blocks: typing.List[Block]

def get_newsletter():
    return db["newsletter"]

def get_user(id):
    return db["users"]

@strawberry.type
class Query:
    @strawberry.field
    def users(self, id: str=None) -> typing.List[User]:
        return db["users"]

@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_user(self, id: str) -> bool:
        db["users"].append(User(id = id, newsletter = []))
        return True

    @strawberry.mutation
    def create_newsletter(self, userid: str) -> bool:
        for user in db["users"]:
            if user.id == userid:
                id = str(uuid.uuid4())
                newsletter = Newsletter(id = id, blocks = [])
                user.newsletter.append(newsletter)
                db["newsletter"].append(newsletter)
                return True
        return False

    @strawberry.mutation
    def create_block(self, newsletterid: str, subreddit: str, flairs: typing.List[str], count: int, upvote_ratio: float) -> bool:
        for newsletter in db["newsletter"]:
            if newsletter.id == newsletterid:
                id = str(uuid.uuid4())
                block = Block(id = id, subreddit = subreddit, flairs= flairs, count= count, upvote_ratio= upvote_ratio)
                newsletter.blocks.append(block)
                db["blocks"].append(block)
                return True
        return False

schema = strawberry.Schema(query=Query, mutation=Mutation)


