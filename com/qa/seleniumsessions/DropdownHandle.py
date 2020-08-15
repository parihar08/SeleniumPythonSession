from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://www.orangehrm.com/orangehrm-30-day-trial/")

def send_data(ele,data):
    driver.find_element(By.ID,ele).send_keys(data)

def select_values(element,value):
    select = Select(element)
    select.select_by_visible_text(value)

def select_value_from_drop_down(element,value):
    options =driver.find_elements(By.XPATH, element)
    print(len(options))
    for ele in options:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

print(driver.title)

driver.maximize_window()

username_url = 'Form_submitForm_subdomain'
first_name= 'Form_submitForm_FirstName'
last_name = 'Form_submitForm_LastName'
email = 'Form_submitForm_Email'
feature_link = driver.find_element(By.LINK_TEXT,'Features')

indus_drop = driver.find_element(By.ID,'Form_submitForm_Industry')
select = Select(indus_drop)

country_drop = driver.find_element(By.ID,'Form_submitForm_Country')
select1 = Select(country_drop)

state_drop= '//select[@id="Form_submitForm_State"]/option'




send_data(username_url,'Naveen Automation Labs')
send_data(first_name,'Naveen')
send_data(last_name,'Automation Labs')
send_data(email,'naveen@automation.com')
#feature_link.click()

#select.select_by_visible_text('Education')
#select.select_by_index(4)
#select.select_by_value('Electronics')
#print(select.is_multiple)

#select1.select_by_visible_text('India')

select_values(indus_drop,'Education')
select_values(country_drop,'India')

#Getting all values from dropdown list and selecting specific one
select2 = Select(indus_drop)
indus_list = select2.options
for elem in indus_list:
    print(elem.text)
    if elem.text=='Automotive':
        elem.click()
        break

#Selecting from dropdown without Select class

country_options = driver.find_elements(By.XPATH,'//select[@id="Form_submitForm_Country"]/option')
print(len(country_options))
for ele in country_options:
    print(ele.text)
    if ele.text== 'Canada':
        ele.click()
        break

time.sleep(2)

select_value_from_drop_down(state_drop,'Alberta')

time.sleep(2)
driver.quit()
