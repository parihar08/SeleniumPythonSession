from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://mail.rediff.com/cgi-bin/login.cgi/")
driver.maximize_window()
time.sleep(3)

'''Alert Javscript Popup'''

signup_ele=driver.find_element(By.NAME,"proceed")
signup_ele.click()
alert=driver.switch_to.alert
print(alert.text)
time.sleep(1)
alert.accept()   #accept the popup
#alert.dismiss()  #cancel the popup
#alert.send_keys("hi")

driver.switch_to.default_content()

time.sleep(2)
driver.quit()