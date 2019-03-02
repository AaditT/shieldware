from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
from sightengine.client import SightengineClient

client = SightengineClient('630881392', 'St5TPUomwvLYq7eiXd4G')
web_api = Client(auto_patch=True, drop_incompat_keys=False)

def checkDrugs(my_url_list):
    my_drug_list = []
    for my_url in my_url_list:
        output = client.check('wad').set_url(my_url)
        drugs = output['drugs']
        my_drug_list.append(drugs)
    return my_drug_list

def checkWeapons(my_url_list):
    my_weapon_list = []
    for my_url in my_url_list:
        output = client.check('wad').set_url(my_url)
        weapons = output['weapon']
        my_weapon_list.append(weapons)
    return my_weapon_list

def checkAlcohol(my_url_list):
    my_alcohol_list = []
    for my_url in my_url_list:
        output = client.check('wad').set_url(my_url)
        alcohol = output['alcohol']
        my_alcohol_list.append(alcohol)
    return my_alcohol_list

def gen_list(count):
    my_list = []
    for i in range(count):
        my_list.append(i)
    return my_list
