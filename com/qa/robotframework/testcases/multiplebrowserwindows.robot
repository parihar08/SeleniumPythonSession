*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://www.google.com
${url1}  http://www.facebook.com

*** Test Cases ***

Handling Multiple Browser Windows Test

    open browser    ${url}    ${browser}
    sleep  2
    open browser    ${url1}    ${browser}

    #Switch to Google
    switch browser  1
    ${title}=   get title
    log to console  ${title}

    #Switch to Facebook
    switch browser  2
    ${title1}=   get title
    log to console  ${title1}

    #Switch back to Google
    switch browser  1
    ${title2}=   get title
    log to console  ${title2}

    sleep  2
    close all browsers


*** Keywords ***
