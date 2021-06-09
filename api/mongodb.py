from dataclasses import asdict
from bson.py3compat import reraise
from api.models import Newsletter
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
load_dotenv()


def factory(data):
    return dict(x for x in data if x[1] is not None)


def connect_to_server():
    '''
    FIXME: nicht doppelt verbinden
    returns datenbank im cluster'''
    conn_str = f'mongodb+srv://mngdbuser:{os.environ.get("mongopw")}@newsletter.jpl4r.mongodb.net/newsletter?retryWrites=true&w=majority'
    # set a 5-second connection timeout
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    try:
        # print(client.server_info())
        db = client.newsletter
        posts = db.posts
        return posts
    except Exception:
        print("Unable to connect to the server.")


def create_newsletter(newsletter: Newsletter):
    '''dict (inc user_id) mit änderung am letter, returns post_id'''
    print(dir(newsletter))
    newsletter = asdict(Newsletter, dict_factory=factory)

    print(newsletter)
    try:
        newsletter = connect_to_server()
        post_id = newsletter.insert_one(dict(Newsletter)).inserted_id
        return post_id

    except Exception as e:
        return "newsletter konnte nicht in der db erstellt werden" + str(e)


def get_newsletters(user_id, post_id=None):
    '''wenn nur user_id, werden alle newsletter sonst der 
    spezifische newsletter in einer List returned
    '''
    try:
        posts = connect_to_server()
        if post_id:
            return [posts.find_one({"_id": ObjectId(post_id), "user_id": user_id})]
        else:
            newsletterlist = []
            for post in posts.find({"user_id": user_id}):
                newsletterlist.append(post)
            return newsletterlist

    except Exception:
        return "newsletter konnte nicht in der db gefunden werden"


def delete_newsletter(post_id, user_id):
    try:
        posts = connect_to_server()
        x = posts.delete_many({"_id": ObjectId(post_id), "user_id": user_id})
        return x.deleted_count

    except Exception:
        return "newsletter konnte nicht in der db gelöscht werden"


def changed_newsletter():
    pass
