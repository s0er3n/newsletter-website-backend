from __future__ import annotations
from dataclasses import asdict
from api.models import NewsletterInput, Newsletter
from api.mongodb import get_newsletters, create_newsletter, delete_newsletter, change_newsletter
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


    @strawberry.mutation
    def make_newsletter(self, newsletter: NewsletterInput) -> str:
        return create_newsletter(newsletter)

    @strawberry.mutation
    def remove_newsletter(self, newsletter_id:str) -> str:
        return delete_newsletter(newsletter_id)


    @strawberry.mutation
    def update_newsletter(self, newsletter_id: str, newsletter: NewsletterInput) -> str:
        return change_newsletter(newsletter_id, newsletter)

schema = strawberry.Schema(query=Query, mutation=Mutation)

