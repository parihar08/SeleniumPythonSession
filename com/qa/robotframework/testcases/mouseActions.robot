*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  http://swisnl.github.io/jQuery-contextMenu/demo.html
${url1}  http://testautomationpractice.blogspot.com
${url2}  http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html

*** Test Cases ***

Mouse Actions Test

    open browser    ${url}    ${browser}
    #Right Click on element/ Open the context menu
    open context menu  xpath://span[@class='context-menu-one btn btn-neutral']
    sleep  2

    #Double Click Action
    go to   ${url1}
    double click element  xpath://button[contains(text(),'Copy Text')]
    sleep  2

    #Drag and Drop Action from source to target
    go to   ${url2}
    drag and drop  id:box6   id:box106
    sleep  2
    close all browsers


*** Keywords ***
