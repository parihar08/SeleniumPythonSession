*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://demowebshop.tricentis.com/register

*** Test Cases ***

Selenium Timeout Test

    open browser    ${url}    ${browser}
    #maximize browser window
    ${timeout}=     get selenium timeout  #Check default selenium timeout - 5 secs
    log to console  ${timeout}

    set selenium timeout  8 seconds  #To change default timeout to user specified time
    ${timeout}=     get selenium timeout
    log to console  ${timeout}

    wait until page contains  Register  #This text should be displayed after page load in 8 secs
    select radio button  Gender     M
    input text  name:FirstName  David
    input text  name:LastName   Malan
    input text  name:Email  david@malan.com
    input text  name:Password   davidMalan
    input text  name:ConfirmPassword    davidMalan

    sleep  2
    close browser

*** Keywords ***
