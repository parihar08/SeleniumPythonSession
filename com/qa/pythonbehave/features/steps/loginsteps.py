from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given('I Launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

@when('Open OrangeHRM Homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')

@when('Enter username "{user}" and password "{pwd}"')
def enterCredentials(context,user,pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('Click on Login button')
def clickOnLogin(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User logged on to Dashboard Page')
def verifyDashboardPage(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False,"Test Failed!!!"
    if text == 'Dashboard':
        context.driver.close()
        assert True, "Test Passed!!!"
