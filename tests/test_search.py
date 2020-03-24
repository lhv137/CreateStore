import pytest
import random
import time
from pages.shopify_page import LoginShopify
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from pages import *


@pytest.fixture

def browser():

    driver = Chrome(executable_path= r"C:\Users\PC\Desktop\Document\Driver\chromedriver.exe")

    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver
    
    # driver.quit()

# # Add new Store
# error = True
def test_login_shopify_partner(browser):

    value = ['offers', 'offer','OFFER', 'OFFERS']

    browser.get("https://apps.shopify.com/")

    browser.find_element_by_xpath('//*[@id="ui-app-store-hero__home-search"]/label').send_keys(random.choice(value))

    browser.find_element_by_xpath('//*[@id="ui-app-store-hero__home-search"]/button').click()

    browser.find_element_by_xpath('//*[@title="Go to Sales Box ‑ Shipping & Offers"]').click()
