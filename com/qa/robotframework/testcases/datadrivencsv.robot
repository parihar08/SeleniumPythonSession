*** Settings ***

Library  SeleniumLibrary
Resource  ../resources/login_resources.robot
Library     DataDriver  file=../../../../TestData/LoginDataRobot.csv
Suite Setup  openMyBrowser          #Before every test case
Suite Teardown  quitBrowser         #After every test case
Test Template  Invalid Login

*** Variables ***

${browser}  chrome
${url}  https://admin-demo.nopcommerce.com/


*** Test Cases ***
LoginTestWithExcel using ${username} and ${password}

*** Keywords ***

Invalid Login
    [Arguments]  ${username}    ${password}
    inputUsername  ${username}
    inputPassword  ${password}
    clickLoginBtn
    iserrormsgvisible
    waitFewSeconds