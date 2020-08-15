from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

#Single Selection
def select_values(option,value):
    for ele in option:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

#Multi Selection
def select_multiple_values(options,values):
    for ele in options:
        print(ele.text)
        for k in range(len(values)):
            if ele.text==values[k]:
                ele.click()
                break

#All values Selection
def select_all_values(options,values):
    if not values[0]=='all':
        for ele in options:
            print(ele.text)
            for k in range(len(values)):
                if ele.text==values[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in options:
                ele.click()
        except Exception as e:
            print(e)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID,'justAnInputBox').click()

time.sleep(2)

drop_list=driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')

values_list=['choice 2','choice 3','choice 6 2 1']

values_list1=['all']

# for ele in drop_list:
#     print(ele.text)
#     if ele.text=='choice 2':
#         ele.click()
#         break

# select_values(drop_list,'choice 2')
# select_values(drop_list,'choice 3')
# select_values(drop_list,'choice 6 2 1')

#select_multiple_values(drop_list,values_list)

#select_all_values(drop_list,values_list)
select_all_values(drop_list,values_list1)

time.sleep(2)
driver.quit()