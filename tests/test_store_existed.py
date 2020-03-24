import pytest
from pages.shopify_page import LoginShopify
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from pages import *


@pytest.fixture

def browser():

    driver = Chrome(executable_path= r"C:\Users\PC\Desktop\Document\Driver\chromedriver.exe")

    driver.implicitly_wait(10)

    yield driver
    
    driver.quit()

# # Add new Store

def test_login_shopify_partner(browser):

    email = 'hoangvidct1@gmail.com'
    password = 'vole132465798'
    city = 'Hà Nội'
    zipcode = '5500000'
    value = 'offers'

    shopify_page = LoginShopify(browser)

    browser.maximize_window()
    
    sleep(3)

    shopify_page.load()

    shopify_page.login_page()

    sleep(3)

    shopify_page.set_fill_email(email)

    sleep(3)

    shopify_page.click_btn_next()

    sleep(3)

    shopify_page.set_fill_password(password)

    sleep(3)

    shopify_page.click_btn_log_in()

    sleep(3)

    shopify_page.go_to_store()

    sleep(2)

    shopify_page.store_select()

    sleep(3)

    shopify_page.store_login_select()

    sleep(10)

    browser.switch_to.window(browser.window_handles[1])

    # browser.refresh()

    shopify_page.go_to_app()

    sleep(3)

    shopify_page.visit_store()
    
    sleep(3)

    browser.switch_to.window(browser.window_handles[2])

    browser.refresh()

    shopify_page.fill_value_search(value)

    sleep(3)

    shopify_page.search_app()

    sleep(3)

    shopify_page.select_app()
    browser.refresh()
    # browser.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div/div[6]/form/input[2]').click()
    shopify_page.add_app_sale()

    sleep(5)

    shopify_page.install_app()

    sleep(3)

    shopify_page.select_charge()

    sleep(10)

    shopify_page.charge()

    sleep(3)

    assert 'Dashboard | Sales Box' == browser.title, "Title Failed"

    browser.quit()

