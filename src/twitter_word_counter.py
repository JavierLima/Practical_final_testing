﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nltk.corpus import stopwords

import collections
import twitter
import operator
import os
import requests
import word_counter
        
class twitter_word_counter(object):
    
    def __init__(self,twitter_api,username):
        self.twitter_api = twitter_api
        self.username = username
    
    def get_last_50_tweets(self):
        
        try:
            tweets = self.twitter_api.GetUserTimeline(screen_name = self.username,count = 400, include_rts=False)
        except: 
            return []
        tweets_text = []
        max_tweets = 50
        for i in range(0,len(tweets)):
            if(i is max_tweets):
                break
            tweets_text.append(tweets[i].text)
            
        return tweets_text
    
    def parse_list_tweets_to_string(self,tweets_list):
        
        if(type(tweets_list) is not list):
            raise(TypeError)
            
        tweets_string = ""
        for tweet in tweets_list:
            tweets_string = tweets_string + " " + tweet
        
        return tweets_string
    
    def top_20_repetitive_word_counter(self):
        tweets_text = self.get_last_50_tweets() 

        if(len(tweets_text) is 0):
            return None
        tweets_text = self.parse_list_tweets_to_string(tweets_text)
        values = word_counter(tweets_text)
        
        sorted_list = sorted(values.items(), key=operator.itemgetter(1))
        sorted_list.reverse()
        
        top_20_values = []
        stop_counter_condition = 0
        for i in range(0,len(sorted_list)):
            if(stop_counter_condition==20):
                break
            top_20_values.append(sorted_list[i]) 
            stop_counter_condition += 1 
            
        return top_20_values


def run():
    """Entry point for console_scripts
    """

if __name__ == "__main__":
    run()
