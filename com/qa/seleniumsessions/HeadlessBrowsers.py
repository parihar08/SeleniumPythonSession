from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


options =webdriver.ChromeOptions()
options.headless =True
#options.add_argument('--headless')
options.add_argument('--incognito')
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(10)

driver.get('http://amazon.in')
print(driver.title)

driver.quit()


opt =webdriver.FirefoxOptions()
opt.headless =True
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=opt)


driver.get('http://amazon.in')
print(driver.title)

driver.quit()