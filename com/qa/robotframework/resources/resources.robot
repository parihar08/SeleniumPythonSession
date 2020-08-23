*** Settings ***

Library  SeleniumLibrary

*** Variables ***

*** Keywords ***


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