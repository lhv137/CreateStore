import pytest
import random
import time
from pages.shopify_page import LoginShopify
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from pages import *
from tests.browser import browser

# # Add new Store

def test_login_shopify_partner(browser):

    email = 'hoangvidct1@gmail.com'
    password = 'vole132465798'
    city = ['HP', 'HN', 'SG', 'NY']
    zipcode = ['5500000', '9810423','5454212']
    value = ['offers', 'offer','OFFER', 'OFFERS']
    rnd_value = str(random.randint(1, 100))
    milliseconds = str(round(time.time() * 1000))
    name_store = "test-store-dev-" + rnd_value + milliseconds
    rnd_add = str(random.randint(1,300))
    address = ['ABC Street','CEF Street', 'FGH Street']
    shopify_page = LoginShopify(browser)
    
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

    shopify_page.add_new_store()

    sleep(3)

    shopify_page.select_mode()
    
    sleep(3)

    shopify_page.set_store_name(name_store)

    sleep(5)

    shopify_page.set_passwpord(password)

    sleep(3)

    shopify_page.set_confirm_password(password)

    sleep(3)
    
    shopify_page.set_address(rnd_add + " " + random.choice(address))

    shopify_page.set_city(random.choice(city))

    shopify_page.set_zip_code(random.choice(zipcode))

    shopify_page.select_mode_app()

    sleep(3)

    shopify_page.select_save_btn()

    sleep(20)

    shopify_page.go_to_app()

    sleep(3)

    shopify_page.visit_store()
    
    sleep(3)

    browser.switch_to.window(browser.window_handles[1])

    # browser.refresh()

    shopify_page.fill_value_search(random.choice(value))

    sleep(3)

    shopify_page.search_app()

    sleep(3)

    shopify_page.select_app()

    # browser.refresh()

    shopify_page.add_app_sale()

    sleep(5)

    shopify_page.install_app()

    sleep(3)

    shopify_page.select_charge()

    sleep(10)

    shopify_page.charge()

    sleep(3)

    assert 'Dashboard | Sales Box' == browser.title, "Title Failed"

    sleep(10)

    browser.quit()



# # Add them Store

# def test_add_store_shopify(browser):

#     email = 'alireview.extension@fireapps.vn'
#     password = '123321'
#     city = 'Hà Nội'
#     zipcode = '5500000'

#     shopify_page = LoginShopify(browser)

#     browser.maximize_window()
    
#     sleep(3)

#     shopify_page.load()

#     shopify_page.login_page()

#     sleep(3)

#     shopify_page.set_fill_email(email)

#     sleep(3)

#     shopify_page.click_btn_next()

#     sleep(3)

#     shopify_page.set_fill_password(password)

#     sleep(3)

#     shopify_page.click_btn_log_in()

#     sleep(3)

#     shopify_page.go_to_store()

#     sleep(2)

#     # shopify_page.add_new_store()

#     shopify_page.add_store()

#     sleep(3)

#     shopify_page.select_mode()
    
#     sleep(3)

#     for i in range(1000,9999):

#            name_store = "test-store-dev-" + str(i)

#     shopify_page.set_store_name(name_store)

#     sleep(5)

#     shopify_page.set_passwpord(password)

#     sleep(3)

#     shopify_page.set_confirm_password(password)

#     sleep(3)
    
#     for i in range(100):
#         address = str(i) + 'Quang Trung'

#     shopify_page.set_address(address)

#     shopify_page.set_city(city)

#     shopify_page.set_zip_code(zipcode)

#     shopify_page.select_mode_app()

#     sleep(3)

#     shopify_page.select_save_btn()

#     sleep(15)








