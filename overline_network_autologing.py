from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from credentials import *
import time
import sys

username = overline_username_1
password = overline_password_1

# place credentials here and uncomment it 
#username = "paster login here"
#password = "paster password here here"



print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)
print("Opening window")
#maximize the window size
driver.maximize_window()
time.sleep(3)
#navigate to browserstack.com
driver.get("https://overline.network/app/auth")
time.sleep(5)
print("done")

print("trying to inser username")
uname = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/input[1]")
uname.send_keys(username)
print("trying to inser pass")
pword = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/input[2]")
pword.send_keys(password)

time.sleep(3)
print("trying to hit login button")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div/div[2]/form/button[1]").click()
print("waiting after login")
time.sleep(7)

print("trying to hit close button")
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/button[1]").click()

#def check_exists_by_xpath(xpath):
#    try:
#        webdriver.find_element_by_xpath(xpath)
#    except NoSuchElementException:
#        return False
#    return True

time.sleep(9)
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")

