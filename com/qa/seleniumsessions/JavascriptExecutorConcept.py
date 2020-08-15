from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  #using alias
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

driver.get("https:/www.amazon.in")

#Finding inner text of the page
inner_text = driver.execute_script("return document.documentElement.innerText;")
print(inner_text)

best_sellers = driver.find_element(By.LINK_TEXT,'Best Sellers')

#Creating border
driver.execute_script("arguments[0].style.border = '3px solid red'",best_sellers)

#Scroll into a element
grocery_header_scroll = driver.find_element(By.XPATH,"//span[text()= 'Best Sellers in Grocery & Gourmet Foods']")
driver.execute_script("arguments[0].scrollIntoView(true);",grocery_header_scroll)

#Scroll to top of the page
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

#Click on link through javascript
driver.execute_script("arguments[0].click();",best_sellers)

#Getting title with javascript
title =driver.execute_script("return document.title;")
print(title)

#Refresh the page
driver.execute_script("history.go(0);")

#Get the user Agent information
user_agent=driver.execute_script("return navigator.userAgent;")
print(user_agent)

#Scroll into a element
sign_in_scroll = driver.find_element(By.XPATH,"//span[text()= 'Sign in']")
driver.execute_script("arguments[0].scrollIntoView(true);",sign_in_scroll)

driver.execute_script("arguments[0].click();",sign_in_scroll)

#Entering data to text box -- send keys
driver.execute_script("document.getElementById('ap_email').value='sparihar08@yahoo.com'")

#Generate Alert
#driver.execute_script("alert('Good Morning Dolly!!!');")

#driver.quit()

driver.get("https://app.hubspot.com/login")
form = driver.find_element(By.ID,'hs-login')
driver.execute_script("arguments[0].style.border = '3px solid red'",form)

driver.get("http://classic.crmpro.com/")
#Scrolling to bottom of the page
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#Scroll into view of a specific element
forgot_password = driver.find_element(By.LINK_TEXT,'Forgot Password?')
driver.execute_script("arguments[0].scrollIntoView(true);",forgot_password)

driver.quit()





