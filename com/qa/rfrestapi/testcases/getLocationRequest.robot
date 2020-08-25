*** Settings ***

Library  RequestsLibrary
Library  Collections

*** Variables ***

${browser}  chrome
${baseUrl}  https://rahulshettyacademy.com
${resource}  /maps/api/place/get/json
${key}     qaclick123
${place_id}     08237ccc4b006c8013354da030bc8091

*** Test Cases ***
Get Location Info
    create session  mysession   ${baseUrl}
    ${response}=    get request  mysession  ${resource}?key=${key}&place_id=${place_id}

    log to console  Status Code is: ${response.status_code}
    log to console  Content is: ${response.content}
    log to console  Headers are: ${response.headers}

    #Validations

    ${statusCode}=  convert to string    ${response.status_code}
    should be equal  ${statusCode}  200

    ${body}=  convert to string    ${response.content}
    should contain  ${body}  Frontline house

    ${contentTypeValue}=  get from dictionary    ${response.headers}   Content-Type
    should be equal  ${contentTypeValue}     application/json;charset=UTF-8

*** Keywords ***
