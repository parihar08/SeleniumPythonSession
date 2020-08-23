*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://seleniumhq.github.io/selenium/docs/api/java/index

*** Test Cases ***

Frames Test

    open browser    ${url}    ${browser}
    #maximize browser window
    select frame  packageListFrame   #select frame by either name or id or xpath
    click link  org.openqa.selenium  #Click on link inside frame
    unselect frame                   #Unselects the current selected frame
    sleep  2                         #Unselect is mandatory to switch to another frame

    select frame  packageFrame   #Switch to second frame
    click link  WebDriver
    unselect frame
    sleep  2

    select frame  classFrame     #Switch to third frame
    click link  Help
    unselect frame

    sleep  2
    close browser


*** Keywords ***
