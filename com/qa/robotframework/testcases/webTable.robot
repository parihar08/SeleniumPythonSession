*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://testautomationpractice.blogspot.com

*** Test Cases ***

Web Table Validations Test

    open browser    ${url}    ${browser}
    ${rowsCount}=    get element count  xpath://table[@name='BookTable']/tbody/tr
    log to console  Row count is: ${rowsCount}

    ${columnCount}=    get element count  xpath://table[@name='BookTable']/tbody/tr[1]/th
    log to console  Column count is: ${columnCount}

    ${bookNameValue}=     get text  xpath://table[@name='BookTable']/tbody/tr[5]/td[1]
    log to console  BookName is: ${bookNameValue}

    #Validate the web table content
    table column should contain  xpath://table[@name='BookTable']   2   Author
    log to console  Second Column is Author

    table row should contain    xpath://table[@name='BookTable']   4   Learn JS
    log to console  Fourth Row is Learn JS

    table cell should contain  xpath://table[@name='BookTable']     5   2   Mukesh
    log to console  Fifth Row and Second Column cell is Mukesh

    table header should contain  xpath://table[@name='BookTable']   Subject
    log to console  Table header contains Subject

    sleep  2
    close browser


*** Keywords ***
