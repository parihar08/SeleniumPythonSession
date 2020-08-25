*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem
Library  JSONLibrary

*** Variables ***

${baseUrl}  https://certtransaction.elementexpress.com
${bearerToken}    "Bearer E4F284BFADA11D01A52508ED7B92FFD7EE0905659F5DED06A4B73FC7739B48A287648801"
${file_path}    com/qa/rfrestapi/xmlfiles

*** Test Cases ***
Bearer Authentication Validation

    create session  mysession   ${baseUrl}
    ${headers}=  create dictionary  Authorization=${bearerToken}   Content-Type=text/xml
    ${req_body}=  Get File  ${file_path}/bearerAuthTest.txt

    ${response}=    post request     mysession  /    data=${req_body}    headers=${headers}

    log to console  Response Status Code is: ${response.status_code}
    log to console  Response Content is: ${response.content}
    log to console  Response Headers are: ${response.headers}

    #Validations
    ${statusCode}=  convert to string   ${response.status_code}
    should be equal  ${statusCode}  200

*** Keywords ***
