*** Settings ***

Library  SeleniumLibrary
Resource  ../resources/pageObjectKeywords.robot

*** Variables ***

${browser}  chrome
${url}  https://admin-demo.nopcommerce.com/
${user}     admin@yourstore.com
${pwd}      admin

*** Test Cases ***
Login Test Case
    openMyBrowser  ${url}   ${browser}
    inputUsername  ${user}
    inputPassword  ${pwd}
    clickLoginBtn
    isDashboardPageVisible
    clickLogoutLink
    quitBrowser


*** Keywords ***
