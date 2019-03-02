# https://github.com/mobolic/facebook-sdk/blob/master/examples/get_posts.py

import facebook
import requests

def some_action(post):
    print(post["picture"])

access_token = "9c0d82270c8693d327a0a0dde722fcd5"
user = "BillGates"

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile["id"], "posts")


[some_action(post=post) for post in posts["data"]]
posts = requests.get(posts["paging"]["next"]).json()
