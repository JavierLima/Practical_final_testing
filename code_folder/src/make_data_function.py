#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nltk.corpus import stopwords

import collections
import twitter
import operator
import os
import requests


from __future__ import print_function
from nltk.corpus import stopwords
import json
import sys
from datetime import date
import re
import string
import collections

def make_data(self, filtered_timeline):
        
        counts = {}
        stop_words = set(stopwords.words(self.language))
        for t in filtered_timeline:
            words = t.split()

            for word in words:
                if word not in stop_words:
                    if word in counts:
                        counts[word]['count'] += 1
                        counts[word]['tweetsContaining'].append(t)
                    else:
                        counts[word] = {}
                        counts[word]['count'] = 1
                        counts[word]['tweetsContaining'] = []
                        counts[word]['tweetsContaining'].append(t)


	sorted_keys = sorted(counts, key=lambda x: (counts[x]['count']),reverse=True)
        orderedDict = collections.OrderedDict()
        
        for key in sorted_keys:
            orderedDict[key] = counts[key]
            
        return orderedDict
 


def run():
    """Entry point for console_scripts
    """

if __name__ == "__main__":
    run()
