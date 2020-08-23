*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://www.practiceselenium.com/practice-form.html

*** Test Cases ***

Handling Dropdowns and List Test

    open browser    ${url}    ${browser}
    #maximize browser window
    #Selecting dropdown list
    select from list by label  continents   Australia
    sleep   1
    select from list by index  continents   6
    sleep   1
    #select from list by value  continents   value
    sleep   1
    #ListBox
    select from list by label  selenium_commands    Switch Commands
    sleep   1
    select from list by label  selenium_commands    WebElement Commands
    sleep   1
    unselect from list by label  selenium_commands  Switch Commands
    sleep   1
    close browser

*** Keywords ***
