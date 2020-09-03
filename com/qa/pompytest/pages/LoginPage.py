from com.qa.pompytest.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from com.qa.pompytest.config.config import TestData
from com.qa.pompytest.pages.HomePage import HomePage


class LoginPage(BasePage):

    """By Locators -- Object Repository"""
    EMAIL = (By.ID,"username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")
    SIGN_UP = (By.LINK_TEXT,"Sign up")

    """Constructor of the Page Class"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """This is used to get the page title"""
    def get_login_page_title(self,title):
        return self.get_title(title)

    """This is used to check the signup link"""
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGN_UP)

    """This is used to login to the app"""
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BTN)
        return HomePage(self.driver)
