from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://www.reddit.com')
cookies = driver.get_cookies()

#print(driver.get_cookies())

for cook in cookies:

    print(cook)

print("****************************************")

driver.add_cookie({"name":"python", "domain":"reddit.com","value":"python"})

print(driver.get_cookies())

driver.quit()





