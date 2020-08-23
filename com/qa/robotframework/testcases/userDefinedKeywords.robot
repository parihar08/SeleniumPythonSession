*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://opensource-demo.orangehrmlive.com

*** Test Cases ***

User Defined Keywords Without Arguments Test

    launchBrowser
    enterCredentials
    waitFewSeconds
    quitBrowser

User Defined Keywords With Arguments Test

    launchBrowserWithArguments   ${url}  ${browser}
    enterCredentials
    waitFewSeconds
    quitBrowser

User Defined Keywords With Arguments and Return Value Test

    ${PageTitle}=   launchBrowserWithArgumentsAndReturnValue   ${url}  ${browser}
    log to console  ${PageTitle}
    log  ${PageTitle}               #This will display the title in the default report
    enterCredentials
    waitFewSeconds
    quitBrowser

*** Keywords ***

launchBrowser
    open browser    ${url}    ${browser}

launchBrowserWithArguments
    [Arguments]     ${appurl}   ${appbrowser}
    open browser    ${appurl}   ${appbrowser}

launchBrowserWithArgumentsAndReturnValue
    [Arguments]     ${appurl}   ${appbrowser}
    open browser    ${appurl}   ${appbrowser}
    ${title}=    get title
    [Return]     ${title}

enterCredentials
    input text  id:txtUsername  Admin
    input text  id:txtPassword  admin123

quitBrowser
    close browser

waitFewSeconds
    sleep  2