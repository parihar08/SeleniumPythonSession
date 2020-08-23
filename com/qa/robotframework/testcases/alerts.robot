*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://testautomationpractice.blogspot.com

*** Test Cases ***

Alerts Test

    open browser    ${url}    ${browser}
    #maximize browser window
    click element  xpath://*[@id="HTML9"]/div[1]/button  #opens alert

    #handle alert    accept      #Accept the alert
    #handle alert    dismiss     #Cancel the alert
    #handle alert    leave       #Keeps the alert open
    alert should be present     Press a button!      #Checks the message on the alert
    #alert should not be present     Press a button!   #Checks the message should not be present on the alert
    sleep  2
    close browser

*** Keywords ***
