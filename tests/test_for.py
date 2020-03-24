import pytest
import random
import time
from pages.shopify_page import LoginShopify
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from pages import *
from tests.test_add_store import test_login_shopify_partner


@pytest.fixture

def browser():

    driver = Chrome(executable_path= r"C:\Users\PC\Desktop\Document\Driver\chromedriver.exe")

    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver
    
    driver.quit()

@pytest.mark.repeat(5)

def test_repeat_add_store():
    pass