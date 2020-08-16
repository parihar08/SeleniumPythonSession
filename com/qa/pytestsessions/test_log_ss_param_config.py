from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium import  webdriver
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time
import pytest
import datetime

@pytest.mark.usefixtures('init_driver') #this fixture is defined in conftest.py file
class BaseTest():
    pass

class TestHubSpot(BaseTest):

    logger = LogGen.logGen()

    @pytest.mark.parametrize("username, password",
                             [
                                 ("admin@gmail.com","admin123"),
                                 ("pari_indiana88@yahoo.com","Calgary_88")
                             ])
    def test_login(self,username,password):
        self.logger.info("***********Verify Data Parameterization | Screenshot Capture***************")
        self.logger.info("***********Verify Config Property| Log Generation***************")
        #self.driver.get("https://app.hubspot.com/login")
        self.driver.get(ReadConfig.baseUrl())  #Reading data from config file using config.ini file
        self.logger.info("***********Launching the URL***************")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,'username').send_keys(username)
        self.logger.info("***********Entering Username***************")
        time.sleep(1)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.logger.info("***********Entering Password***************")
        time.sleep(1)
        self.driver.find_element(By.ID, 'loginBtn').click()
        self.logger.info("***********Clicking on Login Button***************")
        time.sleep(1)
        x = datetime.datetime.now()
        hms = x.strftime("%H_%M_%S")
        self.driver.save_screenshot("../../../Screenshots/test_login_"+str(hms)+".png")
        self.logger.info("***********Generating Screenshot***************")
