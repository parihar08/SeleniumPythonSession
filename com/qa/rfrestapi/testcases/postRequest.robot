*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem

*** Variables ***

${browser}  chrome
${baseUrl}  https://rahulshettyacademy.com
${resource}  /maps/api/place/add/json
${key}     qaclick123
${place_id}     f1319a2b1ce3b310d5bb1d94a3367969
${json_path}    com/qa/rfrestapi/jsonfiles

*** Test Cases ***
Add Place Info
    create session  mysession   ${baseUrl}

    ${header}=  create dictionary  Content-Type=application/json; charset=UTF-8

    ${json}  Get Binary File  ${json_path}/addlocation.json


    ${response}=    post request     mysession  ${resource}?key=${key}   data=${json}    headers=${header}

    log to console  Status Code is: ${response.status_code}
    log to console  Content is: ${response.content}
    log to console  Headers are: ${response.headers}

    #Validations

    ${statusCode}=  convert to string    ${response.status_code}
    should be equal  ${statusCode}  200

    ${res_body}=  convert to string    ${response.content}
    should contain  ${res_body}  APP
    should contain  ${res_body}  OK


*** Keywords ***
