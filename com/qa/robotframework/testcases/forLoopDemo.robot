*** Settings ***


*** Variables ***


*** Test Cases ***

ForLoop1 Test
    : FOR   ${i}    IN RANGE    1   10
    \   LOG TO CONSOLE  ${i}

ForLoop2 Test
    :FOR    ${i}    IN  1 2 3 4 5 6 7 8         #Single space will print all values on same line
    \   LOG TO CONSOLE  ${i}

ForLoop3 Test
    :FOR    ${i}    IN  1  2  3  4  5  6  7     #Double space prints all values on different line
    \   LOG TO CONSOLE  ${i}

ForLoop4 with List Test
    @{items}    create list  1  2   3   4   5
    : FOR   ${i}    IN    @{items}
    \   LOG TO CONSOLE  ${i}

ForLoop5 for Strings Test
    : FOR   ${i}    IN  Roger   Novak   Rafael  Serena
    \   LOG TO CONSOLE  ${i}

ForLoop6 for Strings with list Test
    @{names}    create list  Sachin   Brian   Ricky   Kumar
    : FOR   ${i}    IN  @{names}
    \   LOG TO CONSOLE  ${i}

ForLoop7 with Exit Test
    @{values}    create list  1  2   3   4   5   6
    : FOR   ${i}    IN  @{values}
    \   LOG TO CONSOLE  ${i}
    \   exit for loop if  ${i}==3
*** Keywords ***
