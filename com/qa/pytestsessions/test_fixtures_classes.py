from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium import  webdriver
import time
import pytest


#The code before yield keyword will be executed before all test cases  --setup
#The code after yield keyword will be executed after all test cases    --teardown

@pytest.fixture(scope='class')
def init_chrome_driver(request):
    print('------------This is my setup---------------')
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    #Instead of defining global driver, create a request parameter
    request.cls.driver = ch_driver

    yield
    print('------------This is my teardown----------------')
    ch_driver.close()


@pytest.fixture(scope='class')
def init_firefox_driver(request):
    print('------------This is my setup---------------')
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #Instead of defining global driver, create a request parameter
    request.cls.driver = ff_driver

    yield
    print('------------This is my teardown----------------')
    ff_driver.close()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):  #Parent and child relationship in python
    def test_google_chrome_title(self):
        self.driver.get("http://www.google.com/")
        assert  self.driver.title == 'Google'


@pytest.mark.usefixtures("init_firefox_driver")
class Base_FireFox_Test:
    pass

class Test_Google_Firefox(Base_FireFox_Test):  #Parent and child relationship in python

    def test_google_firefox_title(self):
        self.driver.get("http://www.google.com/")
        assert  self.driver.title == 'Google'