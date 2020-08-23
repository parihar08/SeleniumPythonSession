*** Settings ***

Library  SeleniumLibrary
Resource  ../Resources/resources.robot

*** Variables ***

${browser}  chrome
${url}  http://opensource-demo.orangehrmlive.com

*** Test Cases ***

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