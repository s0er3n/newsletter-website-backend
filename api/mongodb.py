from dataclasses import asdict
from api.models import Newsletter, Options, Block, Days
from dotenv import load_dotenv
import os
import strawberry
load_dotenv()

from rethinkdb import RethinkDB
r = RethinkDB()
r.connect( "rethink", 28015).repl()
newsletters = r.db("test").table("newsletters")


def create_newsletter(newsletter: Newsletter) -> str:
    answer = newsletters.insert(asdict(newsletter)).run()
    return str(answer)

def get_newsletters(user_id: strawberry.ID, post_id: str = None):
    if post_id:

        cursor = newsletters.filter(r.row["user_id"] == user_id and r.row["id"] == post_id).run()
    else:
        cursor = newsletters.filter(r.row["user_id"] == user_id).run()

    newsletterlist = []
    for newsletter in cursor:
        print(newsletter["options"])
        newsletterlist.append(Newsletter(newsletter["id"],user_id=newsletter["user_id"], options = Options(time=newsletter["options"]["time"], frequenzy=Days(**newsletter["options"]["frequenzy"])), blocks= [Block(**block) for block in newsletter["blocks"]]))
    return newsletterlist

def delete_newsletter(newsletter_id):
    return str(newsletters.filter(r.row["id"] == newsletter_id).delete().run())


def change_newsletter(newsletter_id, new_newsletter):
    return str(newsletters.filter(r.row["id"] == newsletter_id).update(asdict(new_newsletter)).run())


