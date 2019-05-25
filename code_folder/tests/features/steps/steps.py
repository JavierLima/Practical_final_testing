from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


@given('we visit our localhost')
def go_to_localhost(context):
  context.driver.get('localhost:8000')
  context.driver.implicit_wait(10)
  
@given('write username "{text}"')
def write_username(context,text):
  element = context.driver.find_element_by_xpath('//*[@id="id_your_name"]')#xpath checkbox
  element.send_keys(text)

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
  button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "reset_button")))
  #button = context.driver.find_element_by_id('reset_button')
  button.click()
  
@when('reset checkbox')
def reset_checkbox(context):
  element = context.driver.find_element_by_xpath('//*[@id="id_your_name"]')#xpath checkbox
  element.clear()
  
@when('we try reset')
def press_reset(context):
  button = context.driver.find_element_by_id('reset_button')
  button.click()
  
@then('I see the tittle web Twitter top words finder')
def check_title(context):
  element = context.driver.find_element_by_xpath('/html/body/nav/a')#xpath tittle
  assert element.text == "Twitter top words finder"
     
    
@then('it should have a textfield "{expected}"')
def check_result(context,expected):
  
  element = context.driver.find_element_by_xpath('/html/body/table/tbody')#xpath body
  result_dict = {}

  for row in element.find_elements_by_tag_name('tr'):
    result_dict[row.find_element_by_xpath('td[1]').text] = row.find_element_by_xpath('td[2]').text
  
  assert result_dict == json.loads(expected)


@then('it should have no body')
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