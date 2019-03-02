from flask import *
import twitterdata
import instagramdata
import engine
import instaloader

app = Flask(__name__)

loader = instaloader.Instaloader()


@app.route('/')
def graph():
    return render_template('home.html', title='Home')


@app.route('/tw_graph', methods=['GET', 'POST'])
def tw_graph():
    if request.method == 'POST':
        username = str(request.form['username-tw'])
        all_tweets = twitterdata.get_all_tweets(username)
        tweets_output = engine.getOutput(all_tweets)
        print("Getting drug vals...")
        drug_vals = engine.checkDrugs(tweets_output)
        print("Getting weapon vals...")
        weapon_vals = engine.checkWeapons(tweets_output)
        print("Getting alcohol vals...")
        alcohol_vals = engine.checkAlcohol(tweets_output)
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
def ig_graph():
    if request.method == 'POST':
        username = str(request.form['username-ig'])
        profile = instaloader.Profile.from_username(loader.context, username)
        print(str(profile.userid))
        all_posts = instagramdata.get_all_igposts(str(profile.userid))
        all_output = engine.getOutput(all_posts)
        print(all_posts)
        print("Getting drug vals...")
        drug_vals = engine.checkDrugs(all_output)
        print("Getting weapon vals...")
        weapon_vals = engine.checkWeapons(all_output)
        print("Getting alcohol vals...")
        alcohol_vals = engine.checkAlcohol(all_output)
        x_vals = engine.gen_list(int(len(all_posts)) + 1)
        return render_template(
            'ig_graph.html',
            name = username,
            drug_vals = drug_vals,
            weapon_vals = weapon_vals,
            alcohol_vals = alcohol_vals,
            x_vals = x_vals,
        )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
