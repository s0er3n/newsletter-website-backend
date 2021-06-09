
from bson.py3compat import reraise
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
load_dotenv()


def connect_to_server():
    '''returns datenbank im cluster'''
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
        

def creat_letter(dict):
    '''dict (inc user_id) mit änderung am letter, returns post_id'''
    posts = connect_to_server()
    post_id = posts.insert_one(dict).inserted_id
    return post_id

def read_letters(user_id, post_id = None):
    posts = connect_to_server()
    if post_id:
        return posts.find_one({"_id": ObjectId(post_id), "user_id": user_id})
    else:
        newsletterlist = []
        for post in posts.find({"user_id": user_id}):
            newsletterlist.append(post)
        return newsletterlist

def delete_letter(post_id, user_id):
    posts = connect_to_server()
    x = posts.delete_many({"_id": ObjectId(post_id), "user_id": user_id})
    return x.deleted_count

