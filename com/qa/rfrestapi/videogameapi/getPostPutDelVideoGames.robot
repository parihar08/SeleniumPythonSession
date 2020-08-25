*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem

*** Variables ***

${baseUrl}  http://localhost:8080
${resource}  /app/videogames
${json_path}    com/qa/rfrestapi/jsonfiles

#Note: Change the id everywhere when running this test case without delete request

#Download VideoGameDB API from github:
#https://github.com/james-willett/VideoGameDB
#Go to the location where we have extracted the downloaded zip file and run below command
#cd /Users/Parihar08/Desktop/Study/VideoGameDB-master
#./gradlew bootRun
#Open the below url:
#http://localhost:8080/swagger-ui/index.html#/Video_Games

*** Test Cases ***
TC1:Get Video Games(GET)
    create session  mysession   ${baseUrl}
    ${response}=    get request  mysession  ${resource}

    log to console  Status Code is: ${response.status_code}
    log to console  Content is: ${response.content}
    log to console  Headers are: ${response.headers}

    #Validations

    ${statusCode}=  convert to string    ${response.status_code}
    should be equal  ${statusCode}  200


    ${contentTypeValue}=  get from dictionary    ${response.headers}   content-type
    should be equal  ${contentTypeValue}     application/xml

TC2:Post Video Games(POST)
    create session  mysession   ${baseUrl}

    ${header}=  create dictionary  Content-Type=application/json

    #2 ways of sending data in body
    ${json}  Get Binary File  ${json_path}/addVideoGames.json

    #${json}=    create dictionary   id=89   name=Sandeep   releaseDate=2020-08-23T20:42:39.455Z   reviewScore=0    category=Parihar     rating=Dolly Minhas

    ${postresponse}=    post request     mysession  ${resource}   data=${json}    headers=${header}

    log to console  Status Code is: ${postresponse.status_code}
    log to console  Content is: ${postresponse.content}
    log to console  Headers are: ${postresponse.headers}

    #Validations

    ${statusCode}=  convert to string    ${postresponse.status_code}
    should be equal  ${statusCode}  200

    ${res_body}=  convert to string    ${postresponse.content}
    should contain  ${res_body}  Record Added Successfully


TC3:Get Video Games by id(GET)
    create session  mysession   ${baseUrl}
    ${response}=    get request  mysession  ${resource}/102

    log to console  Status Code is: ${response.status_code}
    log to console  Content is: ${response.content}
    log to console  Headers are: ${response.headers}

    #Validations

    ${statusCode}=  convert to string    ${response.status_code}
    should be equal  ${statusCode}  200

    ${contentTypeValue}=  get from dictionary    ${response.headers}   content-type
    should be equal  ${contentTypeValue}     application/xml

    ${res_body}=  convert to string    ${response.content}
    should contain  ${res_body}  Sandeep
    should contain  ${res_body}  Parihar
    should contain  ${res_body}  Dolly Minhas

TC4:Update an existing Video Game using id(PUT)
    create session  mysession   ${baseUrl}

    ${header}=  create dictionary  Content-Type=application/json

    ${json}=    create dictionary   id=102   name=Sona   releaseDate=2020-08-23T20:42:39.455Z   reviewScore=0    category=Singh     rating=Pushpender Kaur

    ${putresponse}=    put request     mysession  ${resource}/102   data=${json}    headers=${header}

    log to console  Status Code is: ${putresponse.status_code}
    log to console  Content is: ${putresponse.content}
    log to console  Headers are: ${putresponse.headers}

    #Validations

    ${statusCode}=  convert to string    ${putresponse.status_code}
    should be equal  ${statusCode}  200

    ${res_body}=  convert to string    ${putresponse.content}
    should contain  ${res_body}  Sona
    should contain  ${res_body}  Singh
    should contain  ${res_body}  Pushpender Kaur


TC5:Delete Video Games by id(DEL)
    create session  mysession   ${baseUrl}
    ${delresponse}=    delete request  mysession  ${resource}/102

    log to console  Status Code is: ${delresponse.status_code}
    log to console  Content is: ${delresponse.content}
    log to console  Headers are: ${delresponse.headers}

    #Validations

    ${statusCode}=  convert to string    ${delresponse.status_code}
    should be equal  ${statusCode}  200

    ${res_body}=  convert to string    ${delresponse.content}
    should contain  ${res_body}  Record Deleted Successfully


*** Keywords ***
