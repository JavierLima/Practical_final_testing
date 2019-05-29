
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
import collections

#hey

    
class twitter_word_counter(object):
    
    def __init__(self):
        self.twitter_api = twitter.Api('gz2EucWLrJHTX2GjuMFxYN2la','e0vmSGeIlnHWbVGPO2YbfiPMUiZXh9DQDBML2fu0tqOoqylUXx','1115702759888523265-bbLQl3rRdu9beHs1UoyRXUZZfkqWv6','EttVVAmzpgvd6wnSO596xUIEzL7zGmqptXUQm6D2IACKS', tweet_mode='extended')
        self.timeline = []

        
    def __get_last_month_tweets(self,screen_name):
        '''
            Makes petitions to twitter api until all tweets from last month are gathered
            
            @parameters: 
                screen_name: nombre de usuario
            @returns: 
                list with all tweets
        '''
        try:
            self.timeline = self.twitter_api.GetUserTimeline(screen_name=screen_name, count=200,include_rts=False)
        except:
            return[]
            
        earliest_tweet = min(self.timeline, key=lambda x: x.id).id
        self.month = self.timeline[0].created_at.split()[1]
        end = False
        
        while not end:
            try:
                tweets = self.twitter_api.GetUserTimeline(screen_name=screen_name, max_id=earliest_tweet, count=200, include_rts=False)
            except:
                return[]
                
            new_earliest = min(tweets, key=lambda x: x.id).id

            if not tweets or new_earliest == earliest_tweet:
                break
            else:
                earliest_tweet = new_earliest
#                print("getting tweets before:", earliest_tweet)
                
                for t in tweets:
                    if self.__tweet_is_from_last_month(t):
                        self.timeline.append(t)
                    else:
                        end = True
                        break

        return [t.full_text for t in self.timeline]
        
    
    
    def __tweet_is_from_last_month(self,tweet):
        actualmonth = self.month
        today = int(date.today().day) 
        day = int(tweet.created_at.split()[2])
        month = tweet.created_at.split()[1]
        
        return not (month != self.month and day < today)
        
        
    def __filter_text(self,unfiltered_timeline):
        '''
            Removes full timeline punctuation and url text 
            
            @parameters:
                list with raw tweets 
            @returns: 
                list with cleaned tweets
        '''
        
        punctuation= '!#$%&()*+,-./:;<=>¿¡?@[\]^_{|}~"'
        pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        
        unfiltered_timeline = [pattern.sub('',t) for t in unfiltered_timeline] #
        unfiltered_timeline = [t.translate(str.maketrans('', '', punctuation)) for t in unfiltered_timeline]
        
        return unfiltered_timeline
        
        
    def __make_data(self, filtered_timeline, limit=10):
        '''
            Finds word ocurrences in tweets list
            
            @parameters:
                list with cleaned tweets 
            @returns: 
                ordered dictionary with form:
                    
                   {
                        word:
                            {
                                count: 2,
                                tweets: 
                                    [  
                                        'tweet1',
                                        'tweet2'
                                    ]
                            }
                        word2:
                            {
                                count: 4,
                                tweets: 
                                    [  
                                        'tweet1',
                                        'tweet2'
                                    ]
                            }
                    }
                            
                            
        '''
        
        counts = {}
        stop_words = set(stopwords.words('english')).union(stopwords.words('spanish'))
        for tweet in filtered_timeline:
            words = tweet.split()

            for word in words:
                word = word.lower()
                if word not in stop_words:
                    if word in counts:
                        counts[word]['count'] += 1
                        counts[word]['tweetsContaining'].append(tweet)
                    else:
                        counts[word] = {}
                        counts[word]['count'] = 1
                        counts[word]['tweetsContaining'] = []
                        counts[word]['tweetsContaining'].append(tweet)
                        
        
        sorted_keys = sorted(counts, key=lambda x: (counts[x]['count']),reverse=True)
        orderedDict = collections.OrderedDict()
        
        limitCount = 0
        
        for key in sorted_keys:
            orderedDict[key] = counts[key]
            limitCount += 1
            if limitCount == limit:
                break
            
        return orderedDict
        
        
    def get_final_data(self,user):
            timeline = self.__get_last_month_tweets(user)
            filtered_timeline = self.__filter_text(unfiltered_timeline=timeline)
            return self.__make_data(filtered_timeline, limit=10)
        
        


if __name__ == "__main__":

    user_input = sys.argv[1]
    
    twitter_counter = twitter_word_counter()
    
    data = twitter_counter.get_final_data(user_input)
    
