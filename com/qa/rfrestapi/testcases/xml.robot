*** Settings ***

Library  RequestsLibrary
Library  Collections
Library  OperatingSystem
Library  XML

*** Variables ***

${xml_path}    com/qa/rfrestapi/xmlfiles/XMLfile.xml

*** Test Cases ***
XML Validation

    ${xml_obj}=     parse xml   ${xml_path}

    #Validations

    #Check the Single Element Value - Approach 1
    ${firstNameValue}=   get element text  ${xml_obj}    .//employee[1]/firstname
    log to console  ${firstNameValue}
    should be equal     ${firstNameValue}   John

    #Check the Single Element Value - Approach 2
    ${firstNameElement}=   get element    ${xml_obj}    .//employee[2]/firstname
    log to console  ${firstNameElement.text}
    should be equal     ${firstNameElement.text}   Sandeep

    #Check the Single Element Value - Approach 3
    element text should be    ${xml_obj}    Dolly    .//employee[3]/firstname

    #Check number of nodes in XML file
    ${employeeCount}=   get element count   ${xml_obj}  .//employee
    log to console  ${employeeCount}
    should be equal as integers     ${employeeCount}    5

    ${divisionCount}=   get element count   ${xml_obj}  .//employee/division
    log to console  ${divisionCount}
    should be equal as integers     ${divisionCount}    5

    #Check Attribute Presence
    element attribute should be   ${xml_obj}    id  be134   .//employee[5]
    element attribute should be   ${xml_obj}    id  be130   .//employee[1]

    #Get the name and values of Child nodes
    ${childElements}=   get child elements  ${xml_obj}  .//employee[2]
    should not be empty  ${childElements}
    log to console  Child Elements are: ${childElements}

    ${fName}=   get element text  ${childElements[0]}
    log to console  FirstName value is: ${fName}
    should be equal     ${fName}    Sandeep

    ${lName}=   get element text  ${childElements[1]}
    log to console  LastName value is: ${lName}
    should be equal     ${lName}    Parihar

    ${title}=   get element text  ${childElements[2]}
    log to console  Title value is: ${title}
    should be equal     ${title}    Automation Engineer





*** Keywords ***
