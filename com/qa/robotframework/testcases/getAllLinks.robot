*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://www.countries-ofthe-world.com/flags-of-the-world.html

*** Test Cases ***

Get All Links Test

    open browser    ${url}    ${browser}

    #Count number of links on the webpage
    ${allLinksCount}=   get element count  xpath://a
    log to console  ${allLinksCount}
    sleep  2

    #Print the text of all the links on the webpage
    @{listOfLinks}  create list
    : FOR   ${i}    IN RANGE    1   ${allLinksCount}+1
    \   ${linkText}=    get text    xpath:(//a)[${i}]
    \   log to console  ${linkText}

    close browser


*** Keywords ***
