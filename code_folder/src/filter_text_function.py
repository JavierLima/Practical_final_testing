#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
 
def filter_text(unfiltered_timeline):
        if type(unfiltered_timeline)!=list:
            raise TypeError

        punctuation= '!#$%&()*+,-./:;<=>¿¡?@[\]^_{|}~'
        pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

        for t in unfiltered_timeline:
            if type(t)!=str:
                raise TypeError
            pattern.sub('',t)

        unfiltered_timeline = [t.translate(str.maketrans('', '', punctuation)) for t in unfiltered_timeline]
        
        return unfiltered_timeline

def run():
    """Entry point for console_scripts
    """
if __name__ == "__main__":
    run()