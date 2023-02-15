#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from credentials import *
import time

username = seidd_com_login
password = seidd_com_password

# place credentials here and uncomment it 
#username = "paster login here"
#password = "paster password here here"

class SEIDD():
    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver
        self.failed = []

    def open_web_site(self):
        #opening overline.network
        print("Opening window")
        self.driver.get("https://www.seidd.com/#/pages/login/login")
        time.sleep(5)
        self.login()

    def login(self ):
        print("starting login process...")
        self.driver.maximize_window()

        #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        self.driver.find_element(By.CSS_SELECTOR, "uni-view[class='am-u-sm-12-99 pd inputView am-u-sm-centered ov'] input[class='uni-input-input']").send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(self.password)
        time.sleep(3)
        # get element
        self.driver.find_element(By.CSS_SELECTOR, "uni-button[type='primary']").click()
        #-------login process ends
        print("login success...")
        time.sleep(3)
        self.hit_any_button()

    def hit_any_button(self):
        time.sleep(2)
        print("trying to hit any button")
        self.driver.find_element(By.CSS_SELECTOR, ".am-u-sm-12.pd.zzmodel").click()
        time.sleep(1)
        self.hit_start_button()

    def hit_start_button(self):
        # scroll down a bit to needed button
        self.driver.execute_script("window.scrollTo(0, 500)") 
        time.sleep(2)
        print("trying to hit 'Start' button")
        try:
            self.driver.find_element(By.XPATH, "//uni-text[@class='gui-icons']").click()
        except NoSuchElementException:
            print("Failed to hit, button not found...")
            return self.finish_test_close_everything()
        return self.finish_test_close_everything()
        
    
    def finish_test_close_everything(self):
        print ("Closing window in 5s...")
        time.sleep(5)
        self.driver.close()
        self.driver.quit()


def main():
    """A dummy docstring."""
    print("Test Execution Started")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
    )
    SEIDD(username, password, driver).open_web_site()

if __name__ == "__main__":
    main()
