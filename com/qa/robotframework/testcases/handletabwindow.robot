*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://demo.automationtesting.in/Windows.html

*** Test Cases ***

Tabbed Windows Test

    open browser    ${url}    ${browser}
    #maximize browser window
    click element  xpath://*[@id="Tabbed"]/a/button

    select window   title=Sakinalium | Home     #Switching to the tabbed window with title
    sleep  2
    close all browsers


*** Keywords ***
