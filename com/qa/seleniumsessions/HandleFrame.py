from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://www.londonfreelance.org/courses/frames/index.html")
driver.maximize_window()
time.sleep(2)

'''Handling Frames'''
#Pass frame index
#driver.switch_to.frame(2)

#Pass frame name or id
#driver.switch_to.frame('main')

#Create frame element
frame_element=driver.find_element(By.NAME,'main')
driver.switch_to.frame(frame_element)

#To comeback to the original page
driver.switch_to.default_content()
#driver.switch_to.parent_frame()


headerValue=driver.find_element(By.CSS_SELECTOR,'body > h2').text
print(headerValue)

time.sleep(2)
driver.quit()