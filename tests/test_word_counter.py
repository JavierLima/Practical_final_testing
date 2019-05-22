#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from .src.word_counter import word_counter

class KnownValues(unittest.TestCase):
    def test_word_counter_spanish(self):
        self.assertEqual(word_counter("Vamos a llevarnos bien, porque si no va a haber hondonadas de ostias aqui",'spanish'),({'vamos': 1, 'llevarnos': 1,
                                                                                                                   'bien': 1, 'si': 1, 'va': 1,
                                                                                                                   'haber': 1, 'hondonadas': 1,
                                                                                                                   'ostias': 1, 'aqui':1}))

    def test_word_counter_first_input_integer(self):
        with self.assertRaises(TypeError):
            word_counter(1,'spanish')

    def test_word_counter_second_input_integer(self):
        with self.assertRaises(TypeError):
            word_counter("su-machi-gún",1)

    def test_word_counter_first_input_boolean(self):
        with self.assertRaises(TypeError):
            word_counter(True,'spanish')

    def test_word_counter_second_input_boolean(self):
        with self.assertRaises(TypeError):
            word_counter("su-machi-gún",True)

    def test_word_counter_input_dict(self):
        with self.assertRaises(TypeError):
            word_counter({'coche':2, 'libro':1, 'innovacion':3})

    def test_word_counter_first_input_float(self):
        with self.assertRaises(TypeError):
            word_counter(1.1111111,'spanish')

    def test_word_counter_second_input_float(self):
        with self.assertRaises(TypeError):
            word_counter("su-machi-gún",1.11111111111)

    def test_word_counter_word_with_guion(self):
        self.assertEqual(word_counter("su-machi-gún") ,({'su-machi-gún':1}))

    def test_word_counter_word_with_point(self):
        self.assertEqual(word_counter("su.machi.gún") ,({'machi':1, 'gún':1}))

    def test_word_counter_repeat_words(self):
        self.assertEqual(word_counter("el concepto es el concepto",'spanish') ,({'concepto': 2}))

    def test_word_counter_with_capital_letters(self):
        self.assertEqual(word_counter("Muy ProFesiOnal",'spanish') ,({'profesional':1}))

    def test_word_counter_repeat_more_than_one_word(self):
        self.assertEqual(word_counter("dos, policias rebeldes, dos, policias rebeldes, dos",'spanish') ,({'dos': 3, 'policias': 2, 'rebeldes': 2}))

    def test_word_counter_language_default(self):
        self.assertEqual(word_counter("El concepto es el concepto") ,({'concepto': 2}))

    def test_word_counter_equal_caps_lowers(self):
        self.assertEqual(word_counter("El CONCEPTO es el concepto",'spanish') ,({'concepto': 2}))

    def test_word_counter_equal_word_with_accent_mark(self):
        self.assertEqual(word_counter("El CÓNCEPTO es el cóncepto",'spanish') ,({'cóncepto': 2}))

    def test_word_counter_words_with_differents_accent_mark(self):
        self.assertEqual(word_counter("El CóNCEPTO es el concépto",'spanish') ,({'cóncepto': 1, 'concépto':1}))

    def test_word_counter_only_symbols(self):
        self.assertEqual(word_counter("-./?") ,({'-':1}))

    def test_word_counter_only_stopwords(self):
        self.assertEqual(word_counter("en tanto en para por",'spanish') ,None)

    def test_word_counter_only_stopwords_with_caps(self):
        self.assertEqual(word_counter("EN TANTO EN PARA POR",'spanish') ,None)

    def test_word_counter_question_and_exclamation(self):
        self.assertEqual(word_counter("¿No le he dicho ya que soy abogao? Payaso... ¡Idiota!",'spanish') ,({'dicho': 1, 'abogao': 1, 'payaso': 1, 'idiota': 1}))

    def test_word_counter_satisfy_correct_order(self):
        text = "Carmiña que dejo ésto, que es muy estresante.... interesante no! Estresante!"
        text = text + text + text
        self.assertEqual(word_counter(text,'spanish') ,({'estresante': 6, 'carmiña': 3, 'dejo': 3, 'ésto': 3, 'interesante': 3}))

    def test_word_empty_text(self):
        self.assertEqual(word_counter("") ,None)

if __name__ == '__main__':
    unittest.main()
