import pytest

from com.qa.pompytest.tests.test_BaseTest import BaseTest
from com.qa.pompytest.pages.HomePage import HomePage
from com.qa.pompytest.pages.LoginPage import LoginPage
from com.qa.pompytest.config.config import TestData

class Test_Home(BaseTest):

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = self.homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = self.homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_home_page_account_name(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = self.homePage.get_header_value()
        assert account_name == TestData.ACCOUNT_NAME

    def test_home_page_settings_icon(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert self.homePage.get_header_value()
