#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys

#Twitter API credentials

consumer_key = "08YUWBp8lF6AkuDSOPp71LrgY"
consumer_secret = "s1CbY5gqTMsBYrV5jpkgVivjIqfK05wmLVpa44otvziMsgnNhp"
access_key = "1097354523432017920-mWlifS3sup5mWhZLBXXQKuIJ186rSn"
access_secret = "Ad6z0qJPxDMr8rHIJGioJLUxofUTLEML6qva3R8Ip87BK"


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
