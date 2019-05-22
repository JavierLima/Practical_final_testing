#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nltk.corpus import stopwords
from mock import MagicMock

import collections
import twitter
import operator
import os
import requests

def word_counter(text, language = 'spanish'):
    
    if(type(text) is not str or type(language) is not str):
        raise(TypeError)
        
    punctuation_marks = ["?", "¿", "¡", "!", " ", ",", ".", ";", ":","/"]
    
    filtred_text = ""
    
    for letter in text:
        if(letter not in punctuation_marks):
            filtred_text = filtred_text + letter
        else:
            filtred_text = filtred_text + " "
        
    filtred_text = filtred_text.lower().split()
    stop_words = set(stopwords.words(language))
    
    result_words = []
    trash_items = ["https","\\t","co"]
    
    for word in filtred_text:
        if(word not in stop_words and word not in trash_items):
            result_words.append(word)
    
    if(len(result_words) == 0):
        return None
    
    return collections.Counter(result_words)
 


def run():
    """Entry point for console_scripts
    """

if __name__ == "__main__":
    run()
