#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.tdd.top_20_tweets_counter import word_counter

def test_word_counter_spanish():
    assert word_counter("Vamos a llevarnos bien, porque si no va a haber hondonadas de ostias aqui",'spanish') == ({'vamos': 1, 'llevarnos': 1,
                                                                                                               'bien': 1, 'si': 1, 'va': 1,
                                                                                                               'haber': 1, 'hondonadas': 1,
                                                                                                               'ostias': 1, 'aqui':1})
        
def test_word_counter_first_input_integer():
    with pytest.raises(TypeError):
        word_counter(1,'spanish')
   
def test_word_counter_second_input_integer():
    with pytest.raises(TypeError):
        word_counter("su-machi-gún",1)
        
def test_word_counter_first_input_boolean():
    with pytest.raises(TypeError):
        word_counter(True,'spanish')
   
def test_word_counter_second_input_boolean():
    with pytest.raises(TypeError):
        word_counter("su-machi-gún",True)
       
def test_word_counter_input_dict():
    with pytest.raises(TypeError):
        word_counter({'coche':2, 'libro':1, 'innovacion':3})
        
def test_word_counter_first_input_float():
    with pytest.raises(TypeError):
        word_counter(1.1111111,'spanish')
        
def test_word_counter_second_input_float():
    with pytest.raises(TypeError):
        word_counter("su-machi-gún",1.11111111111)
        
def test_word_counter_word_with_guion():
    assert word_counter("su-machi-gún") == ({'su-machi-gún':1})
    
def test_word_counter_word_with_point():
    assert word_counter("su.machi.gún") == ({'machi':1, 'gún':1})
    
def test_word_counter_repeat_words():
    assert word_counter("el concepto es el concepto",'spanish') == ({'concepto': 2})
    
def test_word_counter_with_capital_letters():
    assert word_counter("Muy ProFesiOnal",'spanish') ==({'profesional':1})
    
def test_word_counter_repeat_more_than_one_word():
    assert word_counter("dos, policias rebeldes, dos, policias rebeldes, dos",'spanish') == ({'dos': 3, 'policias': 2, 'rebeldes': 2})
        
def test_word_counter_language_default():
    assert word_counter("El concepto es el concepto") == ({'concepto': 2})
    
def test_word_counter_equal_caps_lowers():
    assert word_counter("El CONCEPTO es el concepto",'spanish') == ({'concepto': 2})
    
def test_word_counter_equal_word_with_accent_mark():
    assert word_counter("El CÓNCEPTO es el cóncepto",'spanish') == ({'cóncepto': 2})
    
def test_word_counter_words_with_differents_accent_mark():
    assert word_counter("El CóNCEPTO es el concépto",'spanish') == ({'cóncepto': 1, 'concépto':1})
    
def test_word_counter_only_symbols():
    assert word_counter("-./?") == ({'-':1})
    
def test_word_counter_only_stopwords():
    assert word_counter("en tanto en para por",'spanish') == None
    
def test_word_counter_only_stopwords_with_caps():
    assert word_counter("EN TANTO EN PARA POR",'spanish') == None
    
def test_word_counter_question_and_exclamation():
    assert word_counter("¿No le he dicho ya que soy abogao? Payaso... ¡Idiota!",'spanish') == ({'dicho': 1, 'abogao': 1, 'payaso': 1, 'idiota': 1})
    
def test_word_counter_satisfy_correct_order():
    text = "Carmiña que dejo ésto, que es muy estresante.... interesante no! Estresante!"
    text = text + text + text
    assert word_counter(text,'spanish') == ({'estresante': 6, 'carmiña': 3, 'dejo': 3, 'ésto': 3, 'interesante': 3})

def test_word_empty_text():
    assert word_counter("") == None
        