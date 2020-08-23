*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://demo.nopcommerce.com/

*** Test Cases ***

InputBox Test
    open browser    ${url}    ${browser}
    #maximize browser window
    title should be  nopCommerce demo store
    click link  xpath://a[@class='ico-login']
    ${"email_txt"}  set variable    id:Email

    element should be visible   ${"email_txt"}
    element should be enabled   ${"email_txt"}
    #element should not be visible  ${"email_txt"}

    sleep  2
    input text  ${"email_txt"}  sandeep.parihar@fcl.crs
    sleep  1
    clear element text  ${"email_txt"}
    sleep  1

    close browser



*** Keywords ***
