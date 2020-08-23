*** Settings ***

Library  SeleniumLibrary
Variables  ../pageobjects/locators.py

*** Variables ***

*** Keywords ***

openMyBrowser
    [Arguments]  ${appurl}    ${appbrowser}
    open browser  ${appurl}    ${appbrowser}

inputUsername
    [Arguments]  ${username}
    input text  ${login_Username}   ${username}

inputPassword
    [Arguments]  ${password}
    input text  ${login_Password}    ${password}

clickLoginBtn
    click element  ${login_Btn}

clickLogoutLink
    click link  ${dash_Logout}

IsErrorMsgVisible
    page should contain  Login was unsuccessful

isDashboardPageVisible
    page should contain  Dashboard

quitBrowser
    close browser

waitFewSeconds
    sleep  2

enterCredentials
    input text  id:Email  admin@yourstore.com
    input text  id:Password  admin