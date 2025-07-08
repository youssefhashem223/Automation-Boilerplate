*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open the url in browser
    [Arguments]    ${page}    ${browser}
    Open browser    ${page}    ${browser}

Wait for and click in the log-in button
    Wait Until Element Is Visible    css=.ceAbGI
    Click Element    xpath=//*[@id="twilight-sticky-footer-root"]/div/article/div/div/div/div/div/div/div/div[3]/button/div/div

Wait for modal to load
    Wait Until Element Is Visible    css=.jAEPQo

Fill up the form
    [Arguments]    ${name}    ${password}    ${email}
    Input Text    id=signup-username    ${name}
    Input Password    id=password-input    ${password}
    
    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[1]/div/select
    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[1]/div/select/option[16]

    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[2]/div/select
    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[2]/div/select/option[3]

    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[3]/div/select
    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[3]/div/select/option[23]

    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[4]/div[1]/div/div[1]/button/div/div

    Input Text    id=email-input    ${email}

    Wait Until Element Is Visible   css=.hsDHTp
    Click Button    css=.hsDHTp

Wait and see the results
    Sleep    15s