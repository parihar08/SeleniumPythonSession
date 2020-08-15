from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://www.reddit.com')
driver.get_screenshot_as_file('reddit_1.png')


driver.quit()

#Full Screenshot -- Make sure your are running in headless mode

opt =webdriver.FirefoxOptions()
opt.headless =True
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=opt)
driver.implicitly_wait(10)

driver.get('http://www.reddit.com')

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('reddit_full_1.png')


driver.quit()