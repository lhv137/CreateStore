from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from pages.locators import *

class LoginShopify:
    URL = 'https://www.shopify.com/partners'

    btn_log_in = (By.XPATH, LOG_IN_BTN_XPATH)
    fill_email = (By.XPATH, FILL_EMAIL_XPATH)
    btn_next = (By.XPATH, BTN_NEXT_XPATH)
    fill_pass = (By.XPATH, FILL_PASS_XPATH)
    login_btn = (By.XPATH, BTN_LOGIN_XPATH)
    store_page = (By.XPATH, STORE_PAGE_XPATH)
    btn_add = (By.XPATH, BTN_ADD_STORE_XPATH)
    btn_select_dev = (By.XPATH, BTN_SELECT_DEV_STORE_XPATH)
    fill_store_name = (By.XPATH, FILL_STORE_NAME_XPATH)
    fill_pass_store = (By.XPATH, FILL_PASS_STORE_XPATH)
    fill_confirm_pass_store = (By.XPATH, FILL_CONFIRM_PASS_STORE_XPATH)
    fill_address = (By.XPATH, FILL_ADDRESS_XPATH)
    fill_city = (By.XPATH, FILL_CITY_XPATH)
    fill_zipcode = (By.XPATH, FILL_ZIPCODE_XPATH)
    btn_select_app = (By.XPATH, BTN_SELECT_TEST_APP_XPATH)
    btn_save = (By.XPATH, BTN_SAVE_XPATH)
    btn_add_again = (By.XPATH,BTN_ADD_STORE_AGAIN_XPATH)
    btn_select_app_module = (By.XPATH, BTN_SELECT_APP_XPATH)
    btn_visit_store = (By.XPATH, BTN_SELECT_VISIT_APP_XPATH)
    fill_search = (By.XPATH, FILL_VALUE_SEARCH_XPATH)
    btn_search = (By.XPATH, BTN_SEARCH_XPATH)
    btn_app = (By.XPATH, SALES_APP_XPATH)
    btn_add_app = (By.XPATH, BTN_ADD_APP_XPATH)
    btn_install = (By.XPATH, BTN_INSTALL_XPATH)
    btn_select_chare = (By.XPATH, BTN_SELECT_CHARGE_XPATH)
    btn_charge = (By.XPATH, BTN_CHARGE_XPATH)
    select_store = (By.XPATH, SELECT_STORE_XPATH)
    btn_login_stote = (By.XPATH , BTN_LOGIN_STORE_XPATH)

    def __init__(self,browser):
        self.browser = browser
    
    # def window_size(browser):
    #     browser.maximize_window()

    def load(self):
        self.browser.get(self.URL)

# Login Shopify Partner
    def login_page(self):
        btn_log_in = self.browser.find_element(*self.btn_log_in)
        btn_log_in.click()

    def set_fill_email(self,email):
        
        fill_email = self.browser.find_element(*self.fill_email)
        fill_email.send_keys(email)

    def click_btn_next(self):
        btn_next = self.browser.find_element(*self.btn_next)
        btn_next.click()

    def set_fill_password(self,password):
        
        fill_pass = self.browser.find_element(*self.fill_pass)
        fill_pass.send_keys(password)

    def click_btn_log_in(self):
        login_btn = self.browser.find_element(*self.login_btn)
        login_btn.click()

    def go_to_store(self):
        store_page = self.browser.find_element(*self.store_page)
        store_page.click()
    
    def add_new_store(self):
        btn_add = self.browser.find_element(*self.btn_add)
        btn_add.click()

    def select_mode(self):
        btn_select_dev = self.browser.find_element(*self.btn_select_dev)
        btn_select_dev.click()

    def set_store_name(self, name):
       fill_store_name = self.browser.find_element(*self.fill_store_name)
       fill_store_name.send_keys(name)

    def set_passwpord(self,password):
        fill_pass_store = self.browser.find_element(*self.fill_pass_store)
        fill_pass_store.send_keys(password)

    def set_confirm_password(self,password):
        fill_confirm_pass_store = self.browser.find_element(*self.fill_confirm_pass_store)
        fill_confirm_pass_store.send_keys(password)

    def set_address(self, address):
        fill_address = self.browser.find_element(*self.fill_address)
        fill_address.send_keys(Keys.CONTROL, "a")
        fill_address.send_keys(Keys.DELETE)
        sleep(1)
        fill_address.send_keys(address)

    def set_city(self,city):
        fill_city = self.browser.find_element(*self.fill_city)
        fill_city.send_keys(Keys.CONTROL, "a")
        fill_city.send_keys(Keys.DELETE)
        sleep(1)
        fill_city.send_keys(city)

    def set_zip_code(self,zipcode):
        fill_zipcode = self.browser.find_element(*self.fill_zipcode)
        fill_zipcode.send_keys(Keys.CONTROL, "a")
        fill_zipcode.send_keys(Keys.DELETE)
        sleep(1)
        fill_zipcode.send_keys(zipcode)

    def select_mode_app(self):
        btn_select_app = self.browser.find_element(*self.btn_select_app)
        btn_select_app.click()

    def select_save_btn(self):
        btn_save = self.browser.find_element(*self.btn_save)
        btn_save.click()

    def add_store(self):
        btn_add_again = self.browser.find_element(*self.btn_add_again)
        btn_add_again.click()

    def go_to_app(self):
        btn_select_app_module = self.browser.find_element(*self.btn_select_app_module)
        btn_select_app_module.click()

    def visit_store(self):
        btn_visit_store = self.browser.find_element(*self.btn_visit_store)
        btn_visit_store.click()

    def fill_value_search(self, value):
        fill_search = self.browser.find_element(*self.fill_search)
        fill_search.send_keys(value)

    def search_app(self):
        btn_search = self.browser.find_element(*self.btn_search)
        btn_search.click()

    def select_app(self):
        btn_app = self.browser.find_element(*self.btn_app)
        btn_app.click()

    def add_app_sale(self):
        btn_add_app = self.browser.find_element(*self.btn_add_app)
        btn_add_app.click()

    def install_app(self):
        btn_install = self.browser.find_element(*self.btn_install)
        btn_install.click()

    def select_charge(self):
        btn_select_chare = self.browser.find_element(*self.btn_select_chare)
        btn_select_chare.click()

    def charge(self):
        btn_charge = self.browser.find_element(*self.btn_charge)
        btn_charge.click()

    def store_select(self):
        select_store = self.browser.find_element(*self.select_store)
        select_store.click()

    def store_login_select(self):
        btn_login_stote = self.browser.find_element(*self.btn_login_stote)
        btn_login_stote.click()