# https://gist.github.com/freimanas/39f3ad9a5f0249c0dc64#file-tweet_image_dumper-py

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

    while len(new_tweets) > 0 and len(new_tweets) < 5:
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

    outtweets = []

    for tweet in alltweets:
        try:
            print(tweet.entities['media'][0]['media_url'])
        except (NameError, KeyError):
            pass
        else:
            outtweets.append(str(tweet.entities['media'][0]['media_url']))
    outtweets = outtweets[:6]
    print(outtweets)
    return outtweets

