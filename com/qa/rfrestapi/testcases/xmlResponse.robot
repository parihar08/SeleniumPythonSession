*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem
Library  XML

*** Variables ***

${baseUrl}    http://thomas-bayer.com
${resource}     /sqlrest/CUSTOMER

*** Test Cases ***
XML Validation

    create session  mysession   ${baseUrl}
    ${response}=    get request  mysession  ${resource}/15
    #Convert response to String format
    ${responseContentString}=  convert to string    ${response.content}
    #Parse the xml
    ${xml_obj}=     parse xml   ${responseContentString}

    log to console  XML Content in String format is: ${xml_obj}

    #Validations

    element text should be  ${xml_obj}  15    .//ID

    ${firstNameValue}=   get element text  ${xml_obj}    .//FIRSTNAME
    log to console  ${firstNameValue}
    should be equal     ${firstNameValue}   Bill

    ${lastNameValue}=   get element    ${xml_obj}    .//LASTNAME
    log to console  ${lastNameValue.text}
    should be equal     ${lastNameValue.text}   Clancy

    #Get the name and values of Child nodes
    ${childElements}=   get child elements  ${xml_obj}
    should not be empty  ${childElements}
    log to console  Child Elements are: ${childElements}

    ${id}=   get element text  ${childElements[0]}
    ${fName}=   get element text  ${childElements[1]}
    ${lName}=   get element text  ${childElements[2]}
    ${street}=   get element text  ${childElements[3]}
    ${city}=   get element text  ${childElements[4]}

    log to console  ID value is: ${id}
    log to console  FirstName value is: ${fName}
    log to console  LastName value is: ${lName}
    log to console  Street value is: ${street}
    log to console  City value is: ${city}

    should be equal     ${id}    15
    should be equal     ${fName}    Bill
    should be equal     ${lName}    Clancy
    should be equal     ${street}    319 Upland Pl.
    should be equal     ${city}    Seattle


*** Keywords ***
