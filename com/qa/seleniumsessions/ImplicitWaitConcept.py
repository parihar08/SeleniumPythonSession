from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#maximum_time_out=10 sec
#dynamic in nature
#Implicit wait will be applied for all the web elements on the page
#Hence, this is also called global wait
#driver.find_element
#driver.find_elements
#Not applicable for title, url, alerts - for that we have to use Explicit wait

driver.get("https://app.hubspot.com/login/")
driver.maximize_window()

user_name=driver.find_element(By.ID,'username')
user_name.send_keys("test@gmai.com")

driver.find_element(By.ID,'password').send_keys("12345")

#driver.implicitly_wait(5)  -- Override Implicit Wait
#driver.implicitly_wait(10) -- Nullify Implicit Wait

driver.quit()