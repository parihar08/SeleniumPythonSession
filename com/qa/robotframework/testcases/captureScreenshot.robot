*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://opensource-demo.orangehrmlive.com

*** Test Cases ***

Capture Screenshot Test

    open browser    ${url}    ${browser}
    sleep  2
    input text  id:txtUsername  Admin
    input text  id:txtPassword  admin123

    #Capture screenshot of specific element at the path mentioned
    capture element screenshot  xpath://*[@id="divLogo"]/img    Screenshots/Robot_Logo.png

    #Capture screenshot entire page at the path mentioned
    capture page screenshot  Screenshots/Robot_Page.png

    sleep  2
    close browser


*** Keywords ***
