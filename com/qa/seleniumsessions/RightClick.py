from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(5)

'''right click/ context click'''

element=driver.find_element(By.XPATH,"//span[text()='right click me']")
action= ActionChains(driver)
action.context_click(element).perform()

right_click_options=driver.find_elements(By.CSS_SELECTOR,'li.context-menu-icon span')

for ele in right_click_options:
    print(ele.text)
    if ele.text=='Copy':
        ele.click()
        break

time.sleep(2)
driver.quit()