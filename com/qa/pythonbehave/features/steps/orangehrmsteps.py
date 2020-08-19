from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given('Launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

@when('Open OrangeHRM Home Page')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')

@then('Verify that the logo present on page')
def verifyLogo(context):
    status =context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('Close Browser')
def closeBrowser(context):
    context.driver.close()