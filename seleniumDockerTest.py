from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

username = "11"
password = "12"

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


time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[1]/button").click()

 
#time.sleep(10)
#driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[1]/button").click()

time.sleep(20)
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")

