from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://cgi-lib.berkeley.edu/ex/fup.html")
driver.maximize_window()
time.sleep(2)

#File upload will only work if type='file' tag is present
driver.find_element(By.NAME,'upfile').send_keys('/Users/Parihar08/Desktop/Data/Javascript.html')

driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(4)
driver.quit()
