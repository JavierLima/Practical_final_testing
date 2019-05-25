from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context,scenario):
    options = Options()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome("/home/travis/JavierLima/Practical_final_testing/chromedriver",options= options)
    context.driver.implicitly_wait(1)

def after_scenario(context,scenario):
    context.driver.close()