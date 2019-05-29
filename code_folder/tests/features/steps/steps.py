from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import json


@given('we visit our localhost')
def go_to_localhost(context):
  context.driver.get('http://localhost:8000')

@given('write username "{text}"')
def write_username(context,text):
  context.driver.find_element_by_xpath('//*[@id="id_your_name"]').send_keys(text)#xpath checkbox

@when('we press search')
def press_search(context):
  button = context.driver.find_element_by_id('search_button')
  button.click()

@when('we press enter')
def press_enter(context):
  element = context.driver.find_element_by_xpath('//*[@id="id_your_name"]')#xpath checkbox
  element.send_keys(Keys.RETURN)
  
@when('we press reset')
def press_reset(context):
  context.driver.find_element_by_id('reset_button').click()
  
@when('reset checkbox')
def reset_checkbox(context):
  element = context.driver.find_element_by_xpath('//*[@id="id_your_name"]')#xpath checkbox
  element.clear()
  
  
@then('I see the tittle web Twitter top words finder')
def check_title(context):
  element = context.driver.find_element_by_xpath('/html/body/nav/a')#xpath tittle
  assert element.text == "Twitter top words finder"
     
    
@then('the webpage content must be shown the word "{expected_word}"')
def check_result_and_get_content(context,expected_word):
  
  element = context.driver.find_elements_by_css_selector('table td')#xpath body
  result_dict = {}
  new_word = True
  new_number = False
  actual_word = ''
  rest_tweets = 0
  
  for i in range(0,len(element)):
    if new_word:
      actual_word = element[i].text
      result_dict[element[i].text] = {}
      result_dict[actual_word]['count'] = '' 
      result_dict[actual_word]['tweetsContaining'] = []
      new_word = False
      new_number = True
      
    elif new_number:
      rest_tweets = int(element[i].text)
      result_dict[actual_word]['count'] = element[i].text
      new_number = False
      
    else:
      result_dict[actual_word]['tweetsContaining'].append(element[i].text)
      rest_tweets -= 1
      
      if rest_tweets is 0:
        new_word = True
      
  context.result_dict = result_dict
  context.key = expected_word
  
  assert result_dict[expected_word] != None

@then('with a frequency of "{expected_number}"')
def chech_frequency(context,expected_number):
  assert context.result_dict[context.key]['count'] == expected_number
  
@then('the word appears in these tweets {expected_tweets}')
def chech_frequency(context,expected_tweets):
  print(type(json.loads(expected_tweets)))
  print(type(context.result_dict[context.key]['tweetsContaining']))
  assert str(context.result_dict[context.key]['tweetsContaining']) == json.loads(expected_tweets)
  
@then('it should have no content')
def catch_no_body_execption(context):
  try:
    context.driver.find_element_by_xpath('/html/body/table/tbody')
    assert False
  except NoSuchElementException:
    assert True
    
@then('no element in checkbox')
def check_empty_checkbox(context):
  element = context.driver.find_element_by_xpath('//*[@id="id_your_name"]')#xpath checkbox
  assert element.text == ''
