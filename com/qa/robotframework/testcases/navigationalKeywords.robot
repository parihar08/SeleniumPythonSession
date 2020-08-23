*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://www.google.com
${url1}  http://www.facebook.com

*** Test Cases ***

Browser Navigation Test

    open browser    ${url}    ${browser}
    ${location}=    get location  #Will return url of the current browser
    log to console  ${location}

    go to   ${url1}
    ${location}=    get location
    log to console  ${location}

    go back
    ${location}=    get location
    log to console  ${location}

    sleep  2
    close all browsers


*** Keywords ***
