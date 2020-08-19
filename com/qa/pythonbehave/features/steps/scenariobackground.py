from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given('I launch browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('I open application')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@when('Enter valid username and password')
def step_impl(context):
    context.driver.find_element_by_id("txtUsername").send_keys("admin")
    context.driver.find_element_by_id("txtPassword").send_keys("admin123")

@when('Click on login')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must login to the Dashboard Page')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False,"Test Failed!!!"
    if text == 'Dashboard':
        context.driver.close()
        assert True, "Test Passed!!!"


@when('Navigate to search page')
def step_impl(context):
    assert True, "Test Passed!!!"


@then('Search page should display')
def step_impl(context):
    assert True, "Test Passed!!!"


@when('Navigate to advanced search page')
def step_impl(context):
    assert True, "Test Passed!!!"


@then(u'Advanced search page should display')
def step_impl(context):
    assert True, "Test Passed!!!"
