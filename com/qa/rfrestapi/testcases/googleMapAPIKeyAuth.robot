*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem
Library  JSONLibrary

*** Variables ***

${baseUrl}  https://maps.googleapis.com
${resource}     /maps/api/place/nearbysearch/json?
#${resource}     /maps/api/place/nearbysearch/xml?

*** Test Cases ***
Google Map Places API Key Authentication Validation

    create session  mysession   ${baseUrl}
    ${params}=  create dictionary  location=-33.8670522,151.1957362     radius=500      types=food      name=harbour    key=AIzaSyCuYcs3cIUGJC-9Qk7J6YGwke9i5NZCIvs

    ${response}=    get request     mysession   ${resource}     params=${params}

    log to console  Response Status Code is: ${response.status_code}
    log to console  Response Content is: ${response.content}
    log to console  Response Headers are: ${response.headers}

    #Validations
    ${statusCode}=  convert to string   ${response.status_code}
    should be equal  ${statusCode}  200

*** Keywords ***
