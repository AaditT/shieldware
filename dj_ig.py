from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError

from sightengine.client import SightengineClient
client = SightengineClient('630881392', 'St5TPUomwvLYq7eiXd4G')
web_api = Client(auto_patch=True, drop_incompat_keys=False)
user_feed_info = web_api.user_feed('232192182')

def checkDrugs(my_url):
    output = client.check('wad').set_url(my_url)
    drugs = output['drugs']
    return drugs

def checkWeapons(my_url):
    output = client.check('wad').set_url(my_url)
    weapons = output['weapon']
    return weapons

def checkAlcohol(my_url):
    output = client.check('wad').set_url(my_url)
    alcohol = output['alcohol']
    return alcohol

def checkCaption(my_url):
    output = client.check('wad').set_url(my_url)
    print(output)

for post in user_feed_info:
    _url = post['node']['display_url']
    _caption = str(post['node']['edge_media_to_caption']['edges'][0]['node']['text'])
    if (checkDrugs(_url) >= 0.5):
        print("Drug Alert!")
    if (checkWeapons(_url) >= 0.5):
        print("Weapon Alert!")
        if "school" in _caption:
            print("School Shooter Alert!")
    if (checkAlcohol(_url) >= 0.5):
        print("Alcohol Alert!")
