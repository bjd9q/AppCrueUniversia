import behave_webdriver
import chromedriver_autoinstaller
from selenium import webdriver


def before_all(context):
    chromedriver_autoinstaller.install()
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    context.behave_driver = behave_webdriver.Chrome(chromedriver_autoinstaller.install(), options=options)


def after_all(context):
    # cleanup after tests run
    context.behave_driver.quit()


