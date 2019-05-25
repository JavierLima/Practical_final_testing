from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context,scenario):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    context.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",options= options)
    context.driver.implicitly_wait(1)

def after_scenario(context,scenario):
    context.driver.close()