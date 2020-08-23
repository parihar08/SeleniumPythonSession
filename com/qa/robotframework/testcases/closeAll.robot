*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser1}  chrome
${browser2}  firefox
${url}  http://demowebshop.tricentis.com/register
${url1}  http://www.google.com
${url2}  http://www.facebook.com

*** Test Cases ***

Close Browser Test

    open browser    ${url}    ${browser1}
    #maximize browser window

    open browser    ${url1}    ${browser2}

    open browser    ${url2}    ${browser1}

    #close browser  #This will close the latest browser which we opened

    close all browsers  #This will close all the open browsers

*** Keywords ***
