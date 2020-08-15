from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()
time.sleep(5)

'''drag and drop'''

source= driver.find_element(By.ID,'draggable')
target= driver.find_element(By.ID,'droppable')
action= ActionChains(driver)
#action.drag_and_drop(source,target).perform()

action.click_and_hold(source).move_to_element(target).release().perform()

time.sleep(2)
driver.quit()