from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

driver.maximize_window()

username_url = driver.find_element(By.ID,'Form_submitForm_subdomain')
first_name= driver.find_element(By.ID,'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID,'Form_submitForm_LastName')
email = driver.find_element(By.ID,'Form_submitForm_Email')
feature_link = driver.find_element(By.LINK_TEXT,'Features')

username_url.send_keys('Naveen Automation Labs')
first_name.send_keys('Naveen')
last_name.send_keys('Automation Labs')
email.send_keys('naveen@automation.com')
feature_link.click()

linksList= driver.find_elements(By.TAG_NAME,'a')
print(len(linksList))

for element in linksList:
    print(element.text)
    print(element.get_attribute('href'))

imageList= driver.find_elements(By.TAG_NAME,'img')
print(len(imageList))

for image in imageList:
    print(image.get_attribute('src'))


time.sleep(2)
driver.quit()




