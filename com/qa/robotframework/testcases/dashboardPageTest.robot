*** Settings ***

Library  SeleniumLibrary
Resource  ../resources/dashboardPageKeywords.robot

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

Dashboard Test Case
    isDashboardPageVisible
    clickPremiumSupportLink
    go back
    clickLogoutLink
    quitBrowser


*** Keywords ***
