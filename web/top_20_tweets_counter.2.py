#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Downloads all tweets from a given user.

Uses twitter.Api.GetUserTimeline to retreive the last 3,200 tweets from a user.
Twitter doesn't allow retreiving more tweets than this through the API, so we get
as many as possible.

t.py should contain the imported variables.
"""

from __future__ import print_function
from __future__ import unicode_literals
from nltk.corpus import stopwords

import json
import sys
from datetime import date
import twitter
import re
import string
import operator
# from nltk.corpus import stopwords
#import nltk
#
#
#import collections
#import twitter
#import operator
#import os
#import sys
#from datetime import date

    
    
class twitter_word_counter(object):
    
    def __init__(self,username, language):
        self.twitter_api = twitter.Api('gz2EucWLrJHTX2GjuMFxYN2la','e0vmSGeIlnHWbVGPO2YbfiPMUiZXh9DQDBML2fu0tqOoqylUXx','1115702759888523265-bbLQl3rRdu9beHs1UoyRXUZZfkqWv6','EttVVAmzpgvd6wnSO596xUIEzL7zGmqptXUQm6D2IACKS')
        self.username = username
        self.language = language
        self.month = ''

    
    def get_tweets(self,screen_name=None):
        
        timeline = self.twitter_api.GetUserTimeline(screen_name=screen_name, count=200)
        earliest_tweet = min(timeline, key=lambda x: x.id).id
        print("getting tweets before:", earliest_tweet)
        
        self.month = timeline[0].created_at.split()[1]
        end = False
        
        while not end:
            
            tweets = self.twitter_api.GetUserTimeline(
                screen_name=screen_name, max_id=earliest_tweet, count=200
            )
            new_earliest = min(tweets, key=lambda x: x.id).id

            if not tweets or new_earliest == earliest_tweet:
                break
            else:
                earliest_tweet = new_earliest
                print("getting tweets before:", earliest_tweet)
                
                for t in tweets:
                    if self.tweet_is_from_last_month(t):
                        timeline.append(t)
                    else:
                        end = True
                        break

        return [t.text for t in timeline]
        
    
                
    def tweet_is_from_last_month(self,tweet):
        actualmonth = self.month
        today = int(date.today().day) 
        
        day = int(tweet.created_at.split()[2])
        month = tweet.created_at.split()[1]
        
        #TODO translate month to integer 
        
        if month != self.month:
            if day < today:
                print(day)
                return False
            else:
                return True
        
        else:
            return True

        
        


if __name__ == "__main__":

#    screen_name = sys.argv[1]
#    print(screen_name)
#    timeline = get_tweets(api=api, screen_name=screen_name)
#    
    
    
    counts = {}


    
    arguments = sys.argv[1:]
    count = len(arguments)
    print(arguments)
    
    model = twitter_word_counter(arguments[0], 'spanish')
#    result = model.top_20_repetitive_word_counter()
    
    timeline = model.get_tweets(screen_name=arguments[0])
    
    stop_words = set(stopwords.words('english'))

        
    timeline = [t.translate(str.maketrans('', '', string.punctuation)) for t in timeline]
    
    for t in timeline:
        print(t)
        
    
    for t in timeline:
        words = t.split()

        for word in words:
            if word not in stop_words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
    
 
    sorted_x = sorted(counts.items(), key=operator.itemgetter(1))
    
    for i in sorted_x:
        print(i)
    
    
    
    
    
    
#    with open('timeline.json', 'w+') as f:
#        for tweet in timeline:
#            f.write(json.dumps(tweet._json))
#            f.write('\n')

##!/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/bin/python3
## -*- coding: utf-8 -*-
#
#from __future__ import unicode_literals
## from nltk.corpus import stopwords
#import nltk
#
#
#import collections
#import twitter
#import operator
#import os
#import sys
#from datetime import date

#
#def word_counter(text, language = 'spanish'):
#    
#    if(type(text) is not str or type(language) is not str):
#        raise(TypeError)
#        
#    punctuation_marks = ["?", "¿", "¡", "!", " ", ",", ".", ";", ":","/"]
#    
#    filtered_text = ""
#    
#    for letter in text:
#        if(letter not in punctuation_marks):
#            filtered_text += letter
#        else:
#            filtered_text = filtered_text + " "
#            
##    print(text)
##    input()
##    print(text.translate(' ',string.punctuation))
##    input()
#        
#    filtered_text = filtered_text.lower().split()
#    stop_words = set(stopwords.words(language))
#    
#    result_words = []
#    trash_items = ["https","\\t","co"]
#    
#    for word in filtered_text:
#        if(word not in stop_words and word not in trash_items):
#            result_words.append(word)
#    
#    if(len(result_words) == 0):
#        return None
#    
#    return collections.Counter(result_words)
# 
#        
#class twitter_word_counter(object):
#    
#    def __init__(self,username, language):
#        self.twitter_api = twitter.Api('gz2EucWLrJHTX2GjuMFxYN2la','e0vmSGeIlnHWbVGPO2YbfiPMUiZXh9DQDBML2fu0tqOoqylUXx','1115702759888523265-bbLQl3rRdu9beHs1UoyRXUZZfkqWv6','EttVVAmzpgvd6wnSO596xUIEzL7zGmqptXUQm6D2IACKS')
#        self.username = username
#        self.language = language
#    
#    def get_last_50_tweets(self):
#        
#
#        try:
#            tweets = self.twitter_api.GetUserTimeline(screen_name = self.username,count = 500, include_rts=False)
#        except: 
#            return []
#            
#        print(date.today().day)
#
#        for t in tweets:
#            print(t.created_at.split()[2])
#            
#            
#        tweets2 = [t.text for t in tweets if t.retweet_count>30000] 
#        
#        tweets_text = []
#        
#        
#        max_tweets = 50
#        for i in range(0,len(tweets)):
#            if(i is max_tweets):
#                break
#            tweets_text.append(tweets[i].text)
#            
#        return tweets_text
#    
#    def parse_list_tweets_to_string(self,tweets_list):
#        
#        if(type(tweets_list) is not list):
#            raise(TypeError)
#            
#        tweets_string = ""
#        for tweet in tweets_list:
#            tweets_string = tweets_string + " " + tweet
#        
#        return tweets_string
#    
#    def top_20_repetitive_word_counter(self):
#        tweets_text = self.get_last_50_tweets() 
#
#        if(len(tweets_text) is 0):
#            return None
#        tweets_text = self.parse_list_tweets_to_string(tweets_text)
#        values = word_counter(tweets_text, self.language)
#        
#        sorted_list = sorted(values.items(), key=operator.itemgetter(1))
#        sorted_list.reverse()
#        
#        top_20_values = []
#        stop_counter_condition = 0
#        for i in range(0,len(sorted_list)):
#            if(stop_counter_condition==20):
#                break
#            top_20_values.append(sorted_list[i]) 
#            stop_counter_condition += 1 
#            
#        return top_20_values
#
#
#





#
#    """Entry point for console_scripts
#    """
#
#if __name__ == "__main__":
#    
#    from nltk.corpus import stopwords
#
#    arguments = sys.argv[1:]
#    count = len(arguments)
#    print(arguments)
#
#    model = twitter_word_counter(arguments[0], 'spanish')
#    result = model.top_20_repetitive_word_counter()
#    print(result)
#    #run()
#
#
#
#

