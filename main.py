from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
from sightengine.client import SightengineClient
from flask import *

client = SightengineClient('630881392', 'St5TPUomwvLYq7eiXd4G')
web_api = Client(auto_patch=True, drop_incompat_keys=False)

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

def gen_list(count):
    my_list = []
    for i in range(count):
        my_list.append(i)
    return my_list

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/ig/<id>')
def graph(id):
    drug_vals = []
    weapon_vals = []
    alcohol_vals = []
    x = 0
    user_feed_info = web_api.user_feed(id)
    for post in user_feed_info:
        x = x + 1
        _url = post['node']['display_url']
        drug_vals.append(checkDrugs(_url))
        weapon_vals.append(checkWeapons(_url))
        alcohol_vals.append(checkAlcohol(_url))
    x_vals=gen_list(x)
    return render_template('ig_graph.html', x_vals=x_vals, drug_vals=drug_vals,weapon_vals=weapon_vals,alcohol_vals=alcohol_vals)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
