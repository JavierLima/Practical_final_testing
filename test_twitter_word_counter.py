#!/usr/bin/env python
# -*- coding: utf-8 -*-


from word_counter import word_counter
from twitter_word_counter import twitter_word_counter

import unittest
from mock import MagicMock
from requests.exceptions import HTTPError

class KnownValues(unittest.TestCase):
    def test_tweets_words_counter_several_tweets(self):
        tweets = ['En tanto en cuanto nos den lo que es nuestro, discutiremos ese concepto con el fin de discutirlo…', 
              'El concepto, es el concepto',
              'El señor Villambrosa, que es un "gentelmán", me dijo que viniera a resolver esto con "pacisfismo", así que A, lo mismo que le digo una cosa le digo la otra, y B…, cuidado, que igual te viene la C…',
              'Bueno, vamos a llevarnos bien porque si no van a haber hondonadas de hostias aquí, ¿eh?',
              '¿No le he dicho ya que soy abogao? Payaso... ¡Idiota!',
              'El concepto, es el concepto',
              'Los hijos estudiando la carrera en los mejores colegios de Kanfort... con aprovechamiento, ¿eh? ¡Ay, Carmiña: tú en Cambados y yo en el País Vasco...!',
              'El concepto, es el concepto',
              'Sí, sí, el señor Villambrosa lo dejó muy claro. Si iba a venir, si no iba a venir... Vamos, que lo dejó clarísimo.',
              'El concepto, es el concepto',
              'Villambrosa, cuidao con el, ¿eh? Villambrosa es un cabrón, tiene mucha pasta... Nada en la ambulancia.']
        twitter_counter = twitter_word_counter(None,None)
        twitter_counter.get_last_50_tweets = MagicMock(return_value=tweets)
        self.assertEqual(twitter_counter.top_20_repetitive_word_counter() ,[('concepto', 9), ('villambrosa', 4), ('eh', 3), ('si', 3), ('venir', 2),
                                                                       ('iba', 2), ('dejó', 2), ('vamos', 2), ('digo', 2), ('señor', 2), 
                                                                       ('ambulancia', 1), ('pasta', 1), ('mucha', 1), ('cabrón', 1), 
                                                                       ('cuidao', 1), ('clarísimo', 1), ('claro', 1), ('vasco', 1), 
                                                                       ('país', 1), ('cambados', 1)])
    
    def test_tweets_words_counter_with_an_account_withouth_tweets(self):
        tweets = []
        twitter_counter = twitter_word_counter(None,None)
        twitter_counter.get_last_50_tweets = MagicMock(return_value=tweets)
        self.assertEqual(twitter_counter.top_20_repetitive_word_counter() ,None)

    def test_tweets_words_counter_with_one_tweet(self):
        tweets = ["El concepto, es el concepto"]
        twitter_counter = twitter_word_counter(None,None)
        twitter_counter.get_last_50_tweets = MagicMock(return_value=tweets)
        self.assertEqual(twitter_counter.top_20_repetitive_word_counter() ,[('concepto', 2)])

    def test_tweets_words_counter_if_twitter_api_fails(self):
        twitter_counter = twitter_word_counter(None,None)
        twitter_counter.get_last_50_tweets = MagicMock(side_effect=HTTPError)
        with self.assertRaises(HTTPError):
            twitter_counter.top_20_repetitive_word_counter()

if __name__ == '__main__':
    unittest.main()

        