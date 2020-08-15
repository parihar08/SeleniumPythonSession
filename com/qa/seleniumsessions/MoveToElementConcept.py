from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.spicejet.com/")
driver.maximize_window()
time.sleep(5)

'''move to element'''

login= driver.find_element(By.ID,'ctl00_HyperLinkLogin')
action= ActionChains(driver)
action.move_to_element(login).perform()

spice_club=driver.find_element(By.LINK_TEXT,'SpiceClub Members')
action.move_to_element(spice_club).perform()

member_login=driver.find_element(By.LINK_TEXT,'Member Login')
member_login.click()

time.sleep(3)
driver.quit()