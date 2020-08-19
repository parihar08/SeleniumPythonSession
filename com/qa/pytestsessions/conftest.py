from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium import  webdriver
import time
import pytest

#@pytest.fixture(params=['chrome','firefox'],scope='class')

@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request,browser):
    if request.param == 'chrome' and browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == 'chrome' and browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install()) #By default Chrome
    request.cls.driver = driver  #Making driver instance available to the complete class
    yield
    driver.close()

#@pytest.fixture()
#def init_driver(browser):
#    if browser == 'chrome':
#        driver = webdriver.Chrome(ChromeDriverManager().install())
#    elif browser == 'firefox':
#        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#    else:
#        driver = webdriver.Chrome(ChromeDriverManager().install()) #By default Chrome
#   return driver


def pytest_addoption(parser):     #This will get the browser value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture(scope='class')
def browser(request):             #This will return the browser value to the setup method
    return request.config.getoption("--browser")

#Adding PyTest HTML Report

#It is a hook for Adding environment info to HTML Report
#def pytest_configure(config):
#    config.metadata['Project Name'] = 'Selenium Python Sessions'
#    config.metadata['Module Name'] = 'Pytest Sessions'
#    config.metadata['Tester'] = 'Sandeep Parihar'

#It is a hook for delete/modify environment info to HTML Report

#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
#    metadata.pop("JAVA_HOME", None)
#    metadata.pop("Plugins", None)

