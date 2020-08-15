from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium import  webdriver
import time
import pytest

@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_chrome_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Test:
    pass

class Test_Google(Base_Test):

    def test_google_title(self):
        self.driver.get("http://www.google.com/")
        assert self.driver.title == 'Google'


    def test_google_url(self):
        self.driver.get("http://www.google.com/")
        assert self.driver.current_url == 'https://www.google.com/'
