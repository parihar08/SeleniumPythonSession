*** Settings ***

*** Variables ***


*** Test Cases ***
TC1 Prepaid Recharge
    [Tags]  Sanity
    log to console  This is prepaid recharge test case

TC2 Postpaid Recharge
    [Tags]  Sanity          #'Tags' is allowed only once. Only the first value is used.
    log to console  This is postpaid recharge test case

TC3 Search Function
    [Tags]  Regression
    log to console  This Search test case

TC4 Advanced Search Function
    [Tags]  Regression
    log to console  This Advanced Search test case

TC5 User Registration Function
    [Tags]  Sanity
    log to console  This User Registration test case

TC6 Login Function
    [Tags]  Sanity
    log to console  This Login test case

TC7 User Settings Function
    [Tags]  Regression
    log to console  This User Settings test case


*** Keywords ***

