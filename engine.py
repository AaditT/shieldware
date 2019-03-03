from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
from sightengine.client import SightengineClient
from creds import client_access, client_key

client = SightengineClient(client_access, client_key)
web_api = Client(auto_patch=True, drop_incompat_keys=False)

def getOutput(my_url_list):
    output_list = []
    for my_url in my_url_list:
        output_list.append(client.check('wad').set_url(my_url))
    for output in output_list:  print(output)
    return output_list

def checkDrugs(output_list):
    my_drug_list = []
    for output in output_list:
        print(output)
        drugs = output['drugs']
        my_drug_list.append(drugs)
    return [x*10 for x in my_drug_list]

def checkWeapons(output_list):
    my_weapon_list = []
    for output in output_list:
        weapons = output['weapon']
        my_weapon_list.append(weapons)
    return [x*10 for x in my_weapon_list]

def checkAlcohol(output_list):
    my_alcohol_list = []
    for output in output_list:
        alcohol = output['alcohol']
        my_alcohol_list.append(alcohol)
    return [x*10 for x in my_alcohol_list]

def gen_list(count):
    my_list = []
    for i in range(count):
        my_list.append(i)
    return my_list
