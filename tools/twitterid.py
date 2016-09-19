# -*- coding: utf-8 -*-
from tweepy import OAuthHandler
from tweepy import API
import sys

def main(screen_name):
        """
        Gets twitter id of given screen name
        Usage: python twitterid.py screen_name
        """
        auth = OAuthHandler("consumer key", "consumer secret")
        api = API(auth)
        user_details = api.get_user(screen_name)
        user_id = user_details.id
        print(user_id)

if __name__ == '__main__':
        screen_name = sys.argv[1]
        main(screen_name)
