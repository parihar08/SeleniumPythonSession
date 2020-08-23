*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://www.countries-ofthe-world.com/flags-of-the-world.html

*** Test Cases ***

Scrolling Test

    open browser    ${url}    ${browser}
    #Scroll to a particular pixel
    execute javascript  window.scrollTo(0,1500)
    sleep  2

    #Scroll till we find particular element
    go to  ${url}
    scroll element into view    xpath:/html//div[@id='content']/div[@class='container']/div[2]/table[1]//img[@alt='Flag of India']
    sleep  2

    #Scroll to a bottom and top of the page
    go to  ${url}
    execute javascript  window.scrollTo(0,document.body.scrollHeight)  #End of Page
    sleep  2
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)  #Start of Page
    sleep  2
    close browser


*** Keywords ***
