*** Settings ***
Library  SeleniumLibrary



*** Variables ***

${browser}  chrome
${url}  https://demo.nopcommerce.com/

*** Test Cases ***

LoginTest
    #create webdriver    Chrome  executable_path='drivers/chromedriver'
    open browser    ${url}    ${browser}
    #click link  xpath://a[@class='ico-login']
    #input text  id:Email  pavanoltraining@gmail.com
    #input text  id:Password  Test@123
    #click element   xpath://input[@class='button-1 login-button']
    loginToApplication
    close browser


*** Keywords ***

loginToApplication
    click link  xpath://a[@class='ico-login']
    sleep   2
    input text  id:Email    pavanoltraining@gmail.com
    input text  id:Password     Test@123
    click element   xpath://input[@class='button-1 login-button']



