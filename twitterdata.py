import tweepy
import csv
import sys

from creds import consumer_key, consumer_secret, access_key, access_secret

def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name,count=1)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

    outtweets = []

    for tweet in alltweets:
        try:
            print tweet.entities['media'][0]['media_url']
        except (NameError, KeyError):
            pass
        else:
            outtweets.append(str(tweet.entities['media'][0]['media_url']))

    return outtweets
