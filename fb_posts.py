# https://github.com/mobolic/facebook-sdk/blob/master/examples/get_posts.py

import facebook
import requests


def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post["created_time"])

access_token = ""
user = "BillGates"

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile["id"], "posts")

while True:
    try:
        [some_action(post=post) for post in posts["data"]]
        posts = requests.get(posts["paging"]["next"]).json()
    except KeyError:
        break
