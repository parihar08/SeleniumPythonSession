*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${appbrowser}  chrome
${appurl}  https://admin-demo.nopcommerce.com/

*** Keywords ***

openMyBrowser
    open browser  ${appurl}    ${appbrowser}

inputUsername
    [Arguments]  ${username}
    input text  id:Email    ${username}

inputPassword
    [Arguments]  ${password}
    input text  id:Password    ${password}

clickLoginBtn
    click element  xpath://input[@class='button-1 login-button']

clickLogoutLink
    click link  logout

IsErrorMsgVisible
    page should contain  Login was unsuccessful

isDashboardPageVisible
    page should contain  Dashboard

quitBrowser
    close browser

waitFewSeconds
    sleep  2

openLoginPage
    go to  ${appurl}

enterCredentials
    input text  id:Email  admin@yourstore.com
    input text  id:Password  admin