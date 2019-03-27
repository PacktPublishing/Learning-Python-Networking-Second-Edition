#! /usr/bin/python3

from time import sleep
from sys import exit
import tweepy
import json

def twitter_connection(file):
        '''Create the object from which the Twitter API will be consumed,
        reading the credentials from a file, defined in path parameter.'''
        (CONSUMER_KEY,
         CONSUMER_SECRET,
         OAUTH_TOKEN,
     OAUTH_TOKEN_SECRET) = open(file, 'r').read().splitlines()

        # We instanced the authorization manager
        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

        return (tweepy.API(auth), auth)


def getTrendingTopics(woeid=1):

        trends = api.trends_place(1)[0]['trends']

        # We extract the name of the trends and return them as a list
        trendList = [trend['name'] for trend in trends]

        return trendList


class StreamListener(tweepy.StreamListener):
        '''When a Tweet matches our targetTerms it will be passed to this function'''
        def on_data(self, data):
                # Asignamos el JSON de los datos a la variable data
                data = json.loads(data)
                print(data['text'])
                return True


        # If we reach the limit of calls alert and wait 10 "
        def on_limit(self, track):
                print('[!] Limit: {0}').format(track)
                sleep(10)


        # In case of an error, interrupt the listener
        # https://dev.twitter.com/overview/api/response-codes
        def on_error(self, status):
                print('[!] Error: {0}').format(status)
                return False


def streamAPI(auth):
        # We instantiate our listener
        listener = StreamListener()
        # We start the streamer with the OAuth object and the listener
        streamer = tweepy.Stream(auth=auth, listener=listener)
        # We define the terms of which we want to track
        targetTerms = ['python']
        # We start the streamer, passing it our trackTerms
        streamer.filter(track=targetTerms)


try:
        api, auth = twitter_connection("credentials.txt")

        print('[*] Trending topics:')

        trendingTopics = getTrendingTopics()

        for topic in trendingTopics:
                print(topic)

        print('\n[*] Starting streamer:')

        streamAPI(auth)

except KeyboardInterrupt as e:
        exit(0)

