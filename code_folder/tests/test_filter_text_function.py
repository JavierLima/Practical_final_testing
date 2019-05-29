#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from mock import MagicMock
from requests.exceptions import HTTPError
from code_folder.src.filter_text_function import filter_text

class KnownValues(unittest.TestCase):
    def test_filter_text_several_tweets(self):
            tweets = ['En tanto en cuanto nos den lo que es nuestro, discutiremos ese concepto con el fin de discutirlo…',
                  'El concepto, es el concepto' ,
                  'El señor Villambrosa, que es un "gentelmán", me dijo que viniera a resolver esto con "pacisfismo", así que A, lo mismo que le digo una cosa le digo la otra, y B…, cuidado, que igual te viene la C…',
                  'Bueno, vamos a llevarnos bien porque si no van a haber hondonadas de hostias aquí, ¿eh?',
                  '¿No le he dicho ya que soy abogao? Payaso... ¡Idiota!',
                  'El concepto, es el concepto',
                  'Los hijos estudiando la carrera en los mejores colegios de Kanfort... con aprovechamiento, ¿eh? ¡Ay, Carmiña: tú en Cambados y yo en el País Vasco...!',
                  'El concepto, es el concepto',
                  'Sí, sí, el señor Villambrosa lo dejó muy claro. Si iba a venir, si no iba a venir... Vamos, que lo dejó clarísimo.',
                  'El concepto, es el concepto',
                  'Villambrosa, cuidao con el, ¿eh? Villambrosa es un cabrón, tiene mucha pasta... Nada en la ambulancia.']

            self.assertEqual(filter_text(tweets) ,['En tanto en cuanto nos den lo que es nuestro discutiremos ese concepto con el fin de discutirlo…', 'El concepto es el concepto', 'El señor Villambrosa que es un "gentelmán" me dijo que viniera a resolver esto con "pacisfismo" así que A lo mismo que le digo una cosa le digo la otra y B… cuidado que igual te viene la C…', 'Bueno vamos a llevarnos bien porque si no van a haber hondonadas de hostias aquí eh', 'No le he dicho ya que soy abogao Payaso Idiota', 'El concepto es el concepto', 'Los hijos estudiando la carrera en los mejores colegios de Kanfort con aprovechamiento eh Ay Carmiña tú en Cambados y yo en el País Vasco', 'El concepto es el concepto', 'Sí sí el señor Villambrosa lo dejó muy claro Si iba a venir si no iba a venir Vamos que lo dejó clarísimo', 'El concepto es el concepto', 'Villambrosa cuidao con el eh Villambrosa es un cabrón tiene mucha pasta Nada en la ambulancia'])


    def test_filter_text_single_tweet_split_by_punctuation_point(self):
        tweets = ['ho!la']

        self.assertEqual(filter_text(tweets) ,['hola'])

    def test_filter_text_single_punctuation_point(self):
            tweets = ['!']

            self.assertEqual(filter_text(tweets) ,[''])

    def test_filter_text_without_tweets(self):
        tweets = []

        self.assertEqual(filter_text(tweets) ,[])

    def test_filter_text_single_int(self):
        tweets = [5]

        with self.assertRaises(TypeError):
            filter_text(tweets)

    def test_filter_text_bool(self):
        tweets = True

        with self.assertRaises(TypeError):
            filter_text(tweets)

if __name__ == '__main__':
    unittest.main()
