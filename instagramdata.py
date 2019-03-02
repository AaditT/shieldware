from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
import itertools

web_api = Client(auto_patch=True, drop_incompat_keys=False)

def get_all_igposts(id):
    posts = []
    user_feed_info = web_api.user_feed(id)

    for post in user_feed_info:
        _url = post['node']['display_url']
    posts.append(_url[:5])
    return posts
