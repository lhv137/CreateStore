import pytest
import random
import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep



def test_login_shopify_partner():

    driver = Chrome(executable_path= r"C:\Users\PC\Desktop\Document\Driver\chromedriver.exe")

    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver
    
    driver.quit()

    # messagebox.showinfo('Message', 'You clicked the Submit button!')
    value = ['offers', 'offer','OFFER', 'OFFERS']
    driver.get("https://apps.shopify.com/")

    driver.find_element_by_xpath('//*[@id="ui-app-store-hero__home-search"]/label').send_keys(random.choice(value))

    driver.find_element_by_xpath('//*[@id="ui-app-store-hero__home-search"]/button').click()

    driver.find_element_by_xpath('//*[@title="Go to Sales Box ‑ Shipping & Offers"]').click()

    driver.quit()


        

        