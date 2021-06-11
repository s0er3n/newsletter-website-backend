from dataclasses import asdict
from bson.py3compat import reraise
from api.models import Newsletter
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import strawberry
load_dotenv()
def factory(data):
    return dict(x for x in data if x[1] is not None)


def connect_to_server():
    '''
    FIXME: nicht doppelt verbinden
    returns datenbank im cluster'''
    conn_str = f'mongodb+srv://newsletter_account:{os.environ.get("mongopw")}@newsletter.jpl4r.mongodb.net/newsletter?retryWrites=true&w=majority'
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
    news = asdict(newsletter)

    print(newsletter)
    try:
        newsletter = connect_to_server()
        post_id = newsletter.insert_one(news).inserted_id
        return post_id

    except Exception as e:
        return "newsletter konnte nicht in der db erstellt werden" + str(e)


def get_newsletters(user_id: strawberry.ID, post_id: str=None) :
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
                print(post)
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


def change_newsletter(post_id, user_id, changing_layer1, change , changing_layer2 = None, block_number = None):
    '''changing_layer2 requiered if dict in blocks must be changed, otherwise error
    '''

    posts = connect_to_server()
    
    try:
        # print(posts.find_one({"_id": ObjectId(post_id), "user_id": user_id})[changing_layer1])
        print(isinstance(posts.find_one({"_id": ObjectId(post_id), "user_id": user_id})[changing_layer1], (list, dict)))

        if isinstance(posts.find_one({"_id": ObjectId(post_id), "user_id": user_id})[changing_layer1], (list, dict)) and changing_layer2 == None:
            return "add search parameter for dict (add changing_layer2)"

        else:    
        
            if isinstance(posts.find_one({"_id": ObjectId(post_id), "user_id": user_id})[changing_layer1], (list, dict)) and changing_layer2 != None:

                newchange = change_dict_in_newsletter(posts.find_one({"_id": ObjectId(post_id), "user_id": user_id})[changing_layer1], changing_layer2, change, block_number)
                print(newchange)
            
            


            elif isinstance(posts.find_one({"_id": ObjectId(post_id), "user_id": user_id})[changing_layer1], (list, dict)) == False:
                newchange = change
                
            posts.update_one({"_id": ObjectId(post_id), "user_id": user_id}, {'$set': {changing_layer1: newchange}}, upsert = True)    

    except Exception:
        return "newsletter in der db konnte nicht bearbeitet werden"


def change_dict_in_newsletter(list, changing_layer2,change, block_number: int = None):
    list[block_number-1][changing_layer2] = change
    return list


