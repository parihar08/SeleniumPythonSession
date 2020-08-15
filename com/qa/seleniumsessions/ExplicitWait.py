from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  #using alias
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

#Explicit wait is available through WebDriverWait Class

driver.get("https://app.hubspot.com/login/")

wait = WebDriverWait(driver,10)

wait.until(ec.title_is('HubSpot Login'))
print(driver.title)

email_id=wait.until(ec.presence_of_element_located((By.ID,'username')))
email_id.send_keys('test@gmail.com')

driver.find_element(By.ID,'password').send_keys('abc@12345')

driver.quit()