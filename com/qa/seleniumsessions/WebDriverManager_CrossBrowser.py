from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#pip3 install webdriver-manager

browserName ='chrome'

if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == 'safari':
    driver = webdriver.Safari()
else:
    print("Please pass the correct browser name: "+browserName)
    raise Exception('Driver not found')

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID,'username').send_keys('naveenanimation30@gmail.com')
driver.find_element(By.ID,'password').send_keys('Test@12345')
driver.find_element(By.ID,'loginBtn').click()

time.sleep(3)
driver.quit()