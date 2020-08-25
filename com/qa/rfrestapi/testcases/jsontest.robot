*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem
Library  JSONLibrary

*** Variables ***

${json_path}    com/qa/rfrestapi/jsonfiles

*** Test Cases ***
TestCase1
    ${jsonObj}=     load json from file  ${json_path}/jsontest.json

    ${nameValue}=   get value from json   ${jsonObj}  $.firstName
    log to console  ${nameValue[0]}
    should be equal  ${nameValue[0]}    John

    ${streetValue}=   get value from json   ${jsonObj}  $.address.StreetName
    log to console  ${streetValue[0]}
    should be equal  ${streetValue[0]}    111 14 Ave

    ${mobileValue}=   get value from json   ${jsonObj}  $.phonenumber[1].number
    log to console  ${mobileValue[0]}
    should be equal  ${mobileValue[0]}    4034048882

*** Keywords ***
