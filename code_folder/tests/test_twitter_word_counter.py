#!/usr/bin/env python
# -*- coding: utf-8 -*-

#librerias
import unittest
from mock import MagicMock
from requests.exceptions import HTTPError
from code_folder.src.twitter_word_counter import twitter_word_counter
from collections import OrderedDict


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
        twitter_counter = twitter_word_counter()
        twitter_counter.get_last_month_tweets = MagicMock(return_value=tweets)
        
        expected = OrderedDict([('concepto', {'count': 9, 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo…', 'El concepto es el concepto', 'El concepto es el concepto', 'El concepto es el concepto', 'El concepto es el concepto', 'El concepto es el concepto', 'El concepto es el concepto', 'El concepto es el concepto', 'El concepto es el concepto']}), ('villambrosa', {'count': 4, 'tweetsContaining': ['El señor Villambrosa que es un gentelmán me dijo que viniera a resolver esto con pacisfismo así que A lo mismo que le digo una cosa le digo la otra y B… cuidado que igual te viene la C…', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo', 'Villambrosa cuidao con el eh Villambrosa es un cabrón tiene mucha pasta Nada en la ambulancia', 'Villambrosa cuidao con el eh Villambrosa es un cabrón tiene mucha pasta Nada en la ambulancia']}), ('si', {'count': 3, 'tweetsContaining': ['Bueno vamos a llevarnos bien porque si no van a haber hondonadas de hostias aquí eh', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo']}), ('eh', {'count': 3, 'tweetsContaining': ['Bueno vamos a llevarnos bien porque si no van a haber hondonadas de hostias aquí eh', 'Los hijos estudiando la carrera en los mejores colegios de Kanfort con aprovechamiento eh Ay Carmiña tú en Cambados y yo en el País Vasco', 'Villambrosa cuidao con el eh Villambrosa es un cabrón tiene mucha pasta Nada en la ambulancia']}), ('señor', {'count': 2, 'tweetsContaining': ['El señor Villambrosa que es un gentelmán me dijo que viniera a resolver esto con pacisfismo así que A lo mismo que le digo una cosa le digo la otra y B… cuidado que igual te viene la C…', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo']}), ('digo', {'count': 2, 'tweetsContaining': ['El señor Villambrosa que es un gentelmán me dijo que viniera a resolver esto con pacisfismo así que A lo mismo que le digo una cosa le digo la otra y B… cuidado que igual te viene la C…', 'El señor Villambrosa que es un gentelmán me dijo que viniera a resolver esto con pacisfismo así que A lo mismo que le digo una cosa le digo la otra y B… cuidado que igual te viene la C…']}), ('vamos', {'count': 2, 'tweetsContaining': ['Bueno vamos a llevarnos bien porque si no van a haber hondonadas de hostias aquí eh', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo']}), ('dejó', {'count': 2, 'tweetsContaining': ['Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo']}), ('iba', {'count': 2, 'tweetsContaining': ['Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo']}), ('venir', {'count': 2, 'tweetsContaining': ['Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo']})])
        self.assertEqual(twitter_counter.get_final_data(None) ,expected)
    def test_tweets_words_counter_with_an_account_withouth_tweets(self):
        tweets = []
        twitter_counter = twitter_word_counter()
        twitter_counter.get_last_month_tweets = MagicMock(return_value=tweets)
        expected=OrderedDict()
        self.assertEqual(twitter_counter.get_final_data(None) ,expected)

    def test_tweets_words_counter_with_one_tweet(self):
        tweets = ["El concepto, es el concepto"]
        twitter_counter = twitter_word_counter()
        twitter_counter.get_last_month_tweets = MagicMock(return_value=tweets)
        expected=OrderedDict([('concepto', {'count': 2, 'tweetsContaining': ['El concepto es el concepto', 'El concepto es el concepto']})])
        self.assertEqual(twitter_counter.get_final_data(None) ,expected)

    def test_tweets_words_counter_if_twitter_api_fails(self):
        twitter_counter = twitter_word_counter()
        twitter_counter.get_last_month_tweets = MagicMock(side_effect=HTTPError)
        with self.assertRaises(HTTPError):
            twitter_counter.get_final_data(None)
			
			
if __name__ == '__main__':
    unittest.main()
	
        