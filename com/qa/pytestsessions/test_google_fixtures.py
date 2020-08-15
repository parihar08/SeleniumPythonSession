from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium import  webdriver
import time
import pytest

driver = None

#The code before yield keyword will be executed before all test cases  --setup
#The code after yield keyword will be executed after all test cases    --teardown

@pytest.fixture(scope='module')
def init_driver():
    global  driver
    print('------------This is my setup---------------')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com/")

    yield
    print('------------This is my teardown----------------')
    driver.quit()

def test_google_title(init_driver):
    assert driver.title == 'Google'

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == 'https://www.google.com/?gws_rd=ssl'