*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem
Library  JSONLibrary

*** Variables ***

${baseUrl}  http://jsonplaceholder.typicode.com
${parameter}    /photos

*** Test Cases ***
Headers Validation
    create session  mysession   ${baseUrl}
    ${response}=    get request  mysession  ${parameter}

    log to console  Headers are: ${response.headers}

    #Headers Validation
    ${contentType}=     get from dictionary  ${response.headers}    Content-Type
    log to console  Header Content Type is: ${contentType}
    should be equal  ${contentType}     application/json; charset=utf-8

    ${contentEncoding}=     get from dictionary  ${response.headers}    Content-Encoding
    log to console  Header Content Encoding is: ${contentEncoding}
    should be equal  ${contentEncoding}     gzip

Cookies Validation
    create session  mysession   ${baseUrl}
    ${response}=    get request  mysession  ${parameter}

    log to console  Cookies are: ${response.cookies}

    #Cookies Validation
    ${cookieValue}=     get from dictionary  ${response.cookies}    __cfduid
    log to console  Cookie Value is: ${cookieValue}

Response Data Validation
    create session  mysession   ${baseUrl}
    ${response}=    get request  mysession  ${parameter}

    log to console  Status Code is: ${response.status_code}
    #log to console  Content is: ${response.content}

    #Validations
    ${statusCode}=  convert to string   ${response.status_code}
    should be equal  ${statusCode}  200

    ${body}=  to json    ${response.content}

    ${albumIdValue}=   get value from json   ${body}  $[0].albumId
    log to console  ${albumIdValue}
    #should be equal  ${albumIdValue}    [1]

    ${idValue}=   get value from json   ${body}  $[1].id
    log to console  ${idValue}
    #should be equal  ${idValue}    [2]

    ${titleValue}=   get value from json   ${body}  $[2].title
    log to console  ${titleValue}
    #should be equal  ${titleValue}    officia porro iure quia iusto qui ipsa ut modi

    ${urlValue}=   get value from json   ${body}  $[3].url
    log to console  ${urlValue}
    #should be equal  ${urlValue}    https://via.placeholder.com/600/d32776

    ${thumbnailUrlValue}=   get value from json   ${body}  $[4].thumbnailUrl
    log to console  ${thumbnailUrlValue}
    #should be equal  ${thumbnailUrlValue}    https://via.placeholder.com/150/f66b97



*** Keywords ***
