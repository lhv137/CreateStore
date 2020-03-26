import pytest
import random
import time
from datetime import datetime
from pages.shopify_page import LoginShopify
from tests.browser import browser
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from pages import *


# # Add new Store
def test_login_shopify_partner(browser):

    email = 'hoangvidct1@gmail.com'
    password = 'vole132465798'
    count = 0
    repeat = 1
    
    # for count in range (10):

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

    for count in range (repeat):
        city = ['HP', 'HN', 'SG', 'NY','MA']
        zipcode = ['5500000', '9810423','5454212','65456213','21321311']
        value = ['offers', 'offer','OFFER', 'OFFERS']
        rnd_value = str(random.randint(1, 100000))
        # time_str = str(round(time.time() * 1000))
        rnd_add = str(random.randint(1,300))
        address = ['ABC street','CEF Street', 'FGH Street','IJK Street', 'AKG Street']
        today = datetime.now()
        time_str = today.strftime("%d%m%Y%H%M%S")
        name_store = "test-store-dev-" + rnd_value +"-"+ time_str

        shopify_page.go_to_store()

        sleep(2)

        shopify_page.add_store()

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

        sleep(5)

        shopify_page.visit_store()
        
        sleep(5)

        browser.switch_to.window(browser.window_handles[1])

        # browser.close()

        shopify_page.fill_value_search(random.choice(value))

        sleep(3)

        shopify_page.search_app()

        sleep(5)

        shopify_page.select_app()

        sleep(5)

        shopify_page.add_app_sale()

        sleep(5)

        shopify_page.install_app()

        sleep(5)

        shopify_page.select_charge()

        sleep(5)

        shopify_page.charge()

        sleep(10)

        assert 'Dashboard | Sales Box' == browser.title, "Title Failed"

        browser.close()

        browser.switch_to.window(browser.window_handles[0])

        sleep(3)

        # browser.close()

        # browser.execute_script("window.history.go(-1)")

        # browser.back()

        # sleep(5)
        
        shopify_page = LoginShopify(browser)

        shopify_page.load()
        
        shopify_page.login_page()

        sleep(3)

    count = count + 1

    if (count > repeat):
        print("Passed with" + repeat + "times added!!!")

        browser.quit()

    
        


    







