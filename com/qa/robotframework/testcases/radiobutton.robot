*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://www.practiceselenium.com/practice-form.html

*** Test Cases ***

Radio Button Test

    open browser    ${url}    ${browser}
    #maximize browser window
    set selenium speed  1seconds
    #Selecting Radio Button
    select radio button  sex    Female     #name=sex   value=Female
    select radio button  exp    5
    #sleep  2
    #Selecting Checkboxes
    select checkbox     BlackTea
    select checkbox     RedTea
    #sleep  2
    #Unselecting Checkboxes
    unselect checkbox     BlackTea
    unselect checkbox     RedTea
    #sleep  2

    close browser


*** Keywords ***
