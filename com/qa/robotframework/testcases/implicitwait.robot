*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://demowebshop.tricentis.com/register

*** Test Cases ***

Implicit wait Test

    open browser    ${url}    ${browser}
    #maximize browser window
    ${implicitwait}=     get selenium implicit wait  #Check default selenium implicit wait - 0 sec
    log to console  ${implicitwait}

    set selenium implicit wait  8 seconds  #To change default implicit wait to user specified time
    ${implicitwait}=     get selenium implicit wait
    log to console  ${implicitwait}

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
