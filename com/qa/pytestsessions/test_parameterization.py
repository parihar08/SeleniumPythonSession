from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium import  webdriver
import time
import pytest

@pytest.mark.usefixtures('init_driver')
class BaseTest():
    pass

class TestHubSpot(BaseTest):

    @pytest.mark.parametrize("username, password",
                             [
                                 ("admin@gmail.com","admin123"),
                                 ("pari_indiana88@yahoo.com","Calgary_88")
                             ])
    def test_login(self,username,password):
        self.driver.get("https://app.hubspot.com/login")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,'username').send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.ID, 'loginBtn').send_keys(username)
        time.sleep(2)