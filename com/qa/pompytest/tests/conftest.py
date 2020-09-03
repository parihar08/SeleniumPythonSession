import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install()) #By default Chrome
    request.cls.driver = driver  #Making driver instance available to the complete class
    yield
    driver.close()