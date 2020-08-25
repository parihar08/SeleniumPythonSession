*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem
Library  JSONLibrary

*** Variables ***

${baseUrl}  https://restcountries.eu/
${resource}  rest/v2/alpha/IN

*** Test Cases ***
Complex JSON Validation
    create session  mysession   ${baseUrl}
    ${response}=    get request  mysession  ${resource}

    log to console  Status Code is: ${response.status_code}
    log to console  Content is: ${response.content}
    log to console  Headers are: ${response.headers}

    #Validations

    ${statusCode}=  convert to string   ${response.status_code}
    should be equal  ${statusCode}  200

    ${body}=  to json    ${response.content}

    #Single Data Validation
    ${countryNameValue}=   get value from json   ${body}  $.name
    log to console  ${countryNameValue[0]}
    should be equal  ${countryNameValue[0]}    India

    #Single data validation in JSON Array
    ${languageValue}=   get value from json   ${body}  $.languages[1].name
    log to console  ${languageValue[0]}
    should be equal  ${languageValue[0]}    English

    #Multiple data validation in JSON Array
    ${borderValue}=   get value from json   ${body}  $.borders
    log to console  ${borderValue[0]}
    #Checking these countries are present in the list
    should contain any  ${borderValue[0]}   AFG     BGD     MMR     CHN
    should not contain any  ${borderValue[0]}   AUS     USA     CAN     RSA
    : FOR   ${i}    IN  ${borderValue}
    \   LOG TO CONSOLE  Multiple Border Countries are: ${i}

*** Keywords ***
