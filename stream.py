# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests
import csv

#Variables that contains the user credentials to access Twitter API
#creds file, 0=access_token,1=access_token_secret,2=consumer_key,3=consumer_secret
creds_file = "creds.txt"
lines = [line.rstrip('\n') for line in open('id.txt')]
jsonout = open("out.json",'w')
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        sdata = {}
        p_json = json.loads(data)
        
        try:
            if str(p_json['user']['id']) in lines:
                sdata['created_at'] = p_json['created_at']
                sdata['timestamp'] = p_json['timestamp_ms'] 
                sdata['name'] = p_json['user']['name']
                sdata['username'] = p_json['user']['screen_name']
                sdata['qt'] = p_json['is_quote_status']
                sdata['rt'] = p_json['retweeted']
                sdata['text'] = p_json['text']
                sdata['coordinates'] = p_json['coordinates']
                sdata['source'] = p_json['source']
                json.dump(data, jsonout, indent=4, sort_keys=True)
                print( sdata )
        except Exception as some_exception:
            pass
        return True

    def on_error(self, status):
        #print status
        pass

if __name__ == '__main__':
    creds = [line.rstrip('\n') for line in open(creds_file)]
        
    l = StdOutListener()
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    auth = OAuthHandler(creds[2],creds[3])
    auth.set_access_token(creds[0],creds[1])
    stream = Stream(auth, l)
    try:
        stream.filter(follow=lines)
    except AttributeError:
        pass










