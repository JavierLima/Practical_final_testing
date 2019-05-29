#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from requests.exceptions import HTTPError
from code_folder.src.make_data_function import make_data
from collections import OrderedDict

class KnownValues(unittest.TestCase):
    def test_make_data_several_tweets(self):
        tweets = ['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo', 'El concepto es el concepto', 'El señor Villambrosa que es un "gentelmán" me dijo que viniera a resolver esto con "pacisfismo" así que A lo mismo que le digo una cosa le digo la otra y B cuidado que igual te viene la C']
        self.assertEqual(make_data(tweets) ,OrderedDict([('concepto', {'count': 3, 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo', 'El concepto es el concepto', 'El concepto es el concepto']}), ('digo', {'count': 2, 'tweetsContaining': ['El señor Villambrosa que es un "gentelmán" me dijo que viniera a resolver esto con "pacisfismo" así que A lo mismo que le digo una cosa le digo la otra y B cuidado que igual te viene la C', 'El señor Villambrosa que es un "gentelmán" me dijo que viniera a resolver esto con "pacisfismo" así que A lo mismo que le digo una cosa le digo la otra y B cuidado que igual te viene la C']}), ('cuanto', {'count': 1, 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo']}), ('den', {'count': 1, 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo']}), ('discutiremos', {'count': 1, 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo']}), ('fin', {'count': 1, 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo']}), ('discutirlo', {'count': 1, 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo']}), ('señor', {'count': 1, 'tweetsContaining': ['El señor Villambrosa que es un "gentelmán" me dijo que viniera a resolver esto con "pacisfismo" así que A lo mismo que le digo una cosa le digo la otra y B cuidado que igual te viene la C']}), ('villambrosa', {'count': 1, 'tweetsContaining': ['El señor Villambrosa que es un "gentelmán" me dijo que viniera a resolver esto con "pacisfismo" así que A lo mismo que le digo una cosa le digo la otra y B cuidado que igual te viene la C']}), ('"gentelmán"', {'count': 1, 'tweetsContaining': ['El señor Villambrosa que es un "gentelmán" me dijo que viniera a resolver esto con "pacisfismo" así que A lo mismo que le digo una cosa le digo la otra y B cuidado que igual te viene la C']})]))


    def test_make_data_several_stopwords(self):
        tweets = ['El el tanto', 'En tanto en en tanto ']
        self.assertEqual(make_data(tweets) ,OrderedDict())


    def test_make_data_several_spaces(self):
        tweets = ['',' ','','',' ','']
        self.assertEqual(make_data(tweets) ,OrderedDict())

if __name__ == '__main__':
    unittest.main()