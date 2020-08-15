from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://amazon.in')
driver.find_element(By.LINK_TEXT,'Best Sellers').click()

driver.back()

driver.forward()

driver.back()

time.sleep(1)

driver.quit()