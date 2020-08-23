*** Settings ***

Library  SeleniumLibrary
Resource  ../resources/login_resources.robot
Suite Setup  openMyBrowser          #Before every test case
Suite Teardown  quitBrowser         #After every test case
Test Template  Invalid Login

*** Variables ***

${browser}  chrome
${url}  https://admin-demo.nopcommerce.com/


*** Test Cases ***  username    password
Correct User Empty password   admin@yourstore.com     ${EMPTY}
Correct User Wrong password   admin@yourstore.com     admin1
Wrong User Wrong password   admin     admin1
Wrong User Empty password   admin@yourstore.com     ${EMPTY}
Wrong User Wrong password   admin     admin1

*** Keywords ***

Invalid Login
    [Arguments]  ${username}    ${password}
    inputUsername  ${username}
    inputPassword  ${password}
    clickLoginBtn
    iserrormsgvisible
    waitFewSeconds

#Valid Login
    #[Arguments]  ${username}    ${password}
    #inputUsername  ${username}
    #inputPassword  ${password}
    #clickLoginBtn
    #isDashboardPageVisible
    #waitFewSeconds