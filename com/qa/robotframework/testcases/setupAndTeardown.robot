*** Settings ***

Suite Setup  log to console     Opening Browser
Suite Teardown  log to console  Closing Browser

Test Setup  log to console  Login to application
Test Teardown  log to console  Logout from application


*** Variables ***


*** Test Cases ***
TC1 Prepaid Recharge
    log to console  This is prepaid recharge test case

TC2 Postpaid Recharge
    log to console  This is postpaid recharge test case

TC3 Search Function
    log to console  This Search test case

TC4 Advanced Search Function
    log to console  This Advanced Search test case


*** Keywords ***

