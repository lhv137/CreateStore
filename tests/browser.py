import pytest
from pages.shopify_page import LoginShopify
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep



@pytest.fixture

def browser():

    driver = Chrome(executable_path= r"C:\Users\PC\Desktop\Document\Driver\chromedriver.exe")
    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver
    
    driver.quit()
