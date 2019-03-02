from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
import itertools
import pprint
pp = pprint.PrettyPrinter(indent=4)

web_api = Client(auto_patch=True, drop_incompat_keys=False)

def get_all_igposts(id):
    posts = []
    user_feed_info = web_api.user_feed(id)
    pp.pprint(user_feed_info)
    for post in user_feed_info:
        pp.pprint(post['node']['display_url'])
        _url = post['node']['display_url']
        posts.append(_url)
    return posts[:6]
