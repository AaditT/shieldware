from __future__ import print_function
import twitter


consumer_key = "08YUWBp8lF6AkuDSOPp71LrgY"
consumer_secret = "s1CbY5gqTMsBYrV5jpkgVivjIqfK05wmLVpa44otvziMsgnNhp"
access_token_key = "1097354523432017920-mWlifS3sup5mWhZLBXXQKuIJ186rSn"
access_token_secret = "Ad6z0qJPxDMr8rHIJGioJLUxofUTLEML6qva3R8Ip87BK"

api = twitter.Api(consumer_key,consumer_secret,access_token_key,access_token_secret)



import json
import sys
import pprint
import html

def get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets
    results = []
    for tweet in timeline:
        results.append({
            "time" : html.unescape(json.dumps(tweet._json["created_at"], indent=4, sort_keys=True)),
            "text" : html.unescape(json.dumps(tweet._json["text"], indent=4, sort_keys=True)),
        })
    return results


printer = pprint.PrettyPrinter(indent=4)
printer.pprint(get_tweets(api=api, screen_name=screen_name))
