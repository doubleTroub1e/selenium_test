#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc 
from credentials import *
import time
import argparse

def get_valid_username(passed_value):
    if passed_value == "1":
        username = overline_username_1
    elif passed_value == "2":
        username = overline_username_2
    elif passed_value == "3":
        username = overline_username_3
    else:
        print("using default username and password")
        username = overline_username_1
    return (username)

def get_valid_password(passed_value):
    if passed_value == "1":
        password = overline_password_1
    elif passed_value == "2":
        password = overline_password_2
    elif passed_value == "3":
        password = overline_password_3
    else:
        print("using default username and password")
        password = overline_password_1
    return (password)


class OVERLINE():
    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver
        self.failed = []

    def open_web_site(self):
        #opening overline.network
        self.driver.get("https://overline.network/app/auth")
        time.sleep(10)
        self.login()

    def login(self):
        print("starting login process...")
        self.driver.maximize_window()

        #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email address']").send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(self.password)
        # get element
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
        #-------login process ends
        print("login success...")
        self.close_pop_up()

    def close_pop_up(self):
        time.sleep(7)
        print("closing pop-up message now")
        self.driver.find_element(By.CSS_SELECTOR, "img[alt='cross-btn']").click()
        self.finish_test_close_everything()

    def finish_test_close_everything(self):
        print ("Closing window in 5s...")
        time.sleep(5)
        self.driver.close()
        self.driver.quit()

def main():
    """A dummy docstring."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username',
        default='1',
        dest='user_c',
        help='Provide username to use. Defaults to overline_username_1',
        type=str
        )
    args = parser.parse_args()
    username = get_valid_username(args.user_c)
    password = get_valid_password(args.user_c)

    print("Test Execution Started, using username " + username )
    options = uc.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--enable-javascript")
    driver = uc.Chrome(use_subprocess=True,  command_executor='http://localhost:4444/wd/hub', options=options) 
    #driver = webdriver.Remote(
    #command_executor='http://localhost:4444/wd/hub',
    #options=options
    #)
    OVERLINE(username, password, driver).open_web_site()

if __name__ == "__main__":
    main()