﻿from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context,scenario):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    context.driver = webdriver.Chrome("driver/chromedriver",options= options)
    context.driver.implicitly_wait(10)

def after_scenario(context,scenario):
    context.driver.close()