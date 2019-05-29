from __future__ import unicode_literals
from nltk.corpus import stopwords

from collections import OrderedDict

def make_data(filtered_timeline, limit=10):
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
        orderedDict = OrderedDict()

        limitCount = 0

        for key in sorted_keys:
            orderedDict[key] = counts[key]
            limitCount += 1
            if limitCount == limit:
                break

        return orderedDict


def run():
    """Entry point for console_scripts
    """

if __name__ == "__main__":
    run()
