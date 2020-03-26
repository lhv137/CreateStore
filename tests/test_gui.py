
import random
import pytest
import tkinter as tk
from datetime import datetime
from selenium.webdriver import Chrome
from pages.shopify_page import LoginShopify
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from tkinter import *
from tkinter import messagebox


# tkWindow = Tk()  
# tkWindow.geometry('400x150')  
# tkWindow.title('PythonExamples.org - Tkinter Example')
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 800, height = 300)
canvas1.pack()
label1 = tk.Label(root, text='Graphical User Interface')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)


# fillNumber = tk.Entry(root)
# canvas1.create_window(400, 100, window=fillNumber) 

entry1 = tk.Entry (root)
canvas1.create_window(400, 100, window=entry1) 
  
# @pytest.fixture

# def browser():

#     driver = Chrome(executable_path= r"C:\Users\PC\Desktop\Document\Driver\chromedriver.exe")
#     driver.maximize_window()

#     # driver.implicitly_wait(10)

#     # yield driver
    
#     # driver.quit()

def showMsg():  

    email = 'hoangvidct1@gmail.com'
    password = 'vole132465798'
    browser = Chrome(executable_path= r"C:\Users\PC\Desktop\Document\Driver\chromedriver.exe")
    browser.maximize_window()
    count = 0
    repeat = entry1.get()

    # messagebox.showinfo('Message', 'You clicked the Submit button!')

    # browser.get("https://apps.shopify.com/")

    # browser.find_element_by_xpath('//*[@id="ui-app-store-hero__home-search"]/label').send_keys(random.choice(value))

    # browser.find_element_by_xpath('//*[@id="ui-app-store-hero__home-search"]/button').click()

    # browser.find_element_by_xpath('//*[@title="Go to Sales Box ‑ Shipping & Offers"]').click()

    # browser.quit()
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

    for count in range (entry1.get()):
        value = ['offers', 'offer','OFFER', 'OFFERS']
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

        if (count > entry1.get()):
            print("Passed with" + repeat + "times added!!!")

        browser.quit()

def showValue():
    repeat = entry1.get()
    label3 = tk.Label(root, text= 'The Square Root of is:' + repeat,font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

# button = tk.Button(
# 	text = 'Submit',
# 	command = showMsg)  
# canvas1.create_window(200, 180, window=button)

 
button1 = tk.Button (root, text=' Run Script ',command=showMsg, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 180, window=button1)
button2 = tk.Button (root, text=' Run Text ',command=showValue, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 220, window=button2)
# button2.pack() 
root.mainloop()