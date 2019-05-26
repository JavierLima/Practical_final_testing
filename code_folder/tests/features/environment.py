﻿from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context,scenario):
    options = Options()
    options.binary_location = '/usr/bin/google-chrome-stable'
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome("driver/chromedriver", options=options)
    context.implicitly_wait(5)

def after_scenario(context,scenario):
    context.driver.close()