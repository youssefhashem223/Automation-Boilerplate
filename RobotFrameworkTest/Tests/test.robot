*** Settings ***
Library    SeleniumLibrary
Library    XML
Resource   ../Keywords/keywords.robot
Resource   ../Resources/variables.robot

*** Test Cases ***
Create account
    Open the url in browser    ${page}    ${browser}
    
    Wait for and click in the log-in button

    Wait for modal to load

    Fill up the form    ${name}    ${password}    ${email}

    Wait and see the results

    [Teardown]    Close Browser