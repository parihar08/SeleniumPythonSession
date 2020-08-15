from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Users/Parihar08/PycharmProjects/SeleniumPythonSession/drivers/chromedriver")

driver.get("http://www.google.com")
title =driver.title

print(title)

driver.find_element(By.NAME,'q').send_keys("India")
time.sleep(1)
optionList= driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(optionList))

for element in optionList:
    print(element.text)
    if element.text == "india population":
        element.click()
        break

time.sleep(5)
driver.quit()

