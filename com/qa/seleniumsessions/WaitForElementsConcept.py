from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  #using alias
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

#Explicit wait is available through WebDriverWait Class

driver.get("http://freshworks.com/")

wait = WebDriverWait(driver,10)
footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'ul.footer-nav li')))
print(len(footer_links))

for link in footer_links:
    print(link.text)

driver.quit()

