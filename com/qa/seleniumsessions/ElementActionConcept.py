from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://classic.crmpro.com/")
driver.maximize_window()
time.sleep(2)

'''send keys and click using Actions class'''

username_ele=driver.find_element(By.NAME,"username")
password_ele=driver.find_element(By.NAME,"password")
login_ele=driver.find_element(By.XPATH,"//input[@type='submit']")

action= ActionChains(driver)

action.send_keys_to_element(username_ele,'batchautomation')
action.send_keys_to_element(password_ele,'test@12345')
action.click(login_ele).perform()

time.sleep(2)
driver.quit()