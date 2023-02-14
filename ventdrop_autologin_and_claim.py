#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from credentials import *
import time

username = ventdrop_login
password = ventdrop_password

# place credentials here and uncomment it 
#username = "paster login here"
#password = "paster password here here"
class VENTDROP():
    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver
        self.failed = []

    def open_web_site(self):
        #opening overline.network
        print("Opening window")
        self.driver.get("https://ventdrop.com/login")
        time.sleep(5)
        self.login()

    def login(self ):
        print("starting login process...")
        self.driver.maximize_window()

        #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        self.driver.find_element(By.ID, 'username').send_keys(self.username)
        self.driver.find_element(By.ID, 'password').send_keys(self.password)
        # get element
        self.driver.find_element(By.NAME, 'submit').click()
        #-------login process ends
        print("login success...")
        self.hit_reward_button()

    def hit_reward_button(self):
        time.sleep(7)
        print("trying to hit REWARD button")
        self.driver.find_element(By.LINK_TEXT, 'Rewards').click()
        self.hit_claim_chips_button()

    def hit_claim_chips_button(self):
        time.sleep(7)
        print("trying to hit 'Claim Chips' button")
        try:
            self.driver.find_element(By.ID, 'cntdwn').click()
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
    VENTDROP(username, password, driver).open_web_site()

if __name__ == "__main__":
    main()
