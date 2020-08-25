*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem
Library  JSONLibrary

*** Variables ***

${baseUrl}  http://restapi.demoqa.com
${parameters}    /authentication/CheckforAuthentication/

*** Test Cases ***
Basic Authentication Validation

    ${auth}=    create list  ToolsQA    TestPassword
    create session  mysession   ${baseUrl}  auth=${auth}
    ${response}=    get request  mysession  ${parameters}

    log to console  Content is: ${response.content}
    log to console  Headers are: ${response.headers}
    log to console  Status Code is: ${response.status_code}

    #Validations
    ${statusCode}=  convert to string   ${response.status_code}
    should be equal  ${statusCode}  200

*** Keywords ***
