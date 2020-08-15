import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  #using alias
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

url=driver.find_element(By.ID,'Form_submitForm_subdomain')
first_name= driver.find_element(By.ID,'Form_submitForm_FirstName')
last_name=driver.find_element(By.ID,'Form_submitForm_LastName')
email_id= driver.find_element(By.ID,'Form_submitForm_Email')
job_title=driver.find_element(By.ID,'Form_submitForm_JobTitle')
company= driver.find_element(By.ID,'Form_submitForm_CompanyName')
phone_number=driver.find_element(By.ID,'Form_submitForm_Contact')
no_of_employees= driver.find_element(By.ID,'Form_submitForm_NoOfEmployees')
industry=driver.find_element(By.ID,'Form_submitForm_Industry')
country= driver.find_element(By.ID,'Form_submitForm_Country')


workbook = xlrd.open_workbook('DataFile.xlsx')
#sheet = workbook.sheet_by_name('login')
sheet = workbook.sheet_by_name('registration')

#get total number of rows

rowCount = sheet.nrows
print(rowCount)

#get total number of columns

colCount = sheet.ncols
print(colCount)

#for curr_row in range(1,rowCount):
   # username = sheet.cell_value(curr_row,0)
   # password = sheet.cell_value(curr_row, 1)

   # print(username + " "+ password)

for curr_row in range(1,rowCount):
    urlValue = sheet.cell_value(curr_row,0)
    firstName = sheet.cell_value(curr_row, 1)
    lastName = sheet.cell_value(curr_row, 2)
    emailId = sheet.cell_value(curr_row, 3)
    jobTitle = sheet.cell_value(curr_row, 4)
    companyName = sheet.cell_value(curr_row, 5)
    phone = sheet.cell_value(curr_row, 6)
    totalEmp = sheet.cell_value(curr_row, 7)
    industryName = sheet.cell_value(curr_row, 8)
    countryName = sheet.cell_value(curr_row, 9)

    print(urlValue +"--> "+ firstName +"--> "+ lastName)

    url.clear()
    url.send_keys(urlValue)
    first_name.clear()
    first_name.send_keys(firstName)
    last_name.clear()
    last_name.send_keys(lastName)
    email_id.clear()
    email_id.send_keys(emailId)
    job_title.clear()
    job_title.send_keys(jobTitle)
    company.clear()
    company.send_keys(companyName)
    phone_number.clear()
    phone_number.send_keys(phone)

    time.sleep(3)

driver.quit()
