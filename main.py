from flask import *
import twitterdata
import instagramdata
import engine

app = Flask(__name__)

@app.route('/')
def graph():
    return render_template('home.html', title='Home')


@app.route('/tw_graph', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        username = str(request.form['username-tw'])
        all_tweets = twitterdata.get_all_tweets(username)
        print("Getting drug vals...")
        drug_vals = engine.checkDrugs(all_tweets)
        print("Getting weapon vals...")
        weapon_vals = engine.checkWeapons(all_tweets)
        print("Getting alcohol vals...")
        alcohol_vals = engine.checkAlcohol(all_tweets)
        x_vals = engine.gen_list(int(len(all_tweets)) + 1)
        return render_template(
            'tw_graph.html',
            name = username,
            drug_vals = drug_vals,
            weapon_vals = weapon_vals,
            alcohol_vals = alcohol_vals,
            x_vals = x_vals
        )

@app.route('/ig_graph', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        username = str(request.form['username-ig'])
        all_posts = instagramdata.get_all_igposts(username)
        print("Getting drug vals...")
        drug_vals = engine.checkDrugs(all_posts)
        print("Getting weapon vals...")
        weapon_vals = engine.checkWeapons(all_posts)
        print("Getting alcohol vals...")
        alcohol_vals = engine.checkAlcohol(all_posts)
        x_vals = engine.gen_list(int(len(all_posts)) + 1)
        return render_template(
            'ig_graph.html',
            name = username,
            drug_vals = drug_vals,
            weapon_vals = weapon_vals,
            alcohol_vals = alcohol_vals,
            x_vals = x_vals
        )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
