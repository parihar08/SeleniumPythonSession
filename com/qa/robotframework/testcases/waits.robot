*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://demowebshop.tricentis.com/register

*** Test Cases ***

Handling Waits and Speed Test

    ${speed}=   get selenium speed  #Checking default timeout of Selenium speed
    log to console  ${speed}
    open browser    ${url}    ${browser}
    #maximize browser window
    #sleep  1
    set selenium speed  1 seconds    #Will be applicable to all steps in the script - default 0
    select radio button  Gender     M
    input text  name:FirstName  David
    input text  name:LastName   Malan
    input text  name:Email  david@malan.com
    input text  name:Password   davidMalan
    input text  name:ConfirmPassword    davidMalan
    ${speed}=   get selenium speed  #Checking timeout of Selenium speed after setting the value
    log to console  ${speed}

    sleep  2

    close browser

*** Keywords ***
