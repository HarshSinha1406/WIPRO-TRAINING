*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    ${CURDIR}/testdata.xlsx    sheet_name=Sheet1    dialect=Excel
Suite Setup       Open Orangehrm
Test Template     Orangehrmlogin With Excel
Suite Teardown    Close All Browsers

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}  chrome

*** Test Cases ***
Login with user from Excel
    [Tags]    DDT

*** Keywords ***
Open Orangehrm
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s

Orangehrmlogin With Excel
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    name=username    10s
    Input Text      name=username    ${username}
    Input Password  name=password    ${password}
    Click Button    xpath=//button[@type="submit"]

    # validate successful login
    Wait Until Page Contains    Dashboard    10s

    # open user dropdown (FIXED XPATH)
    Wait Until Element Is Visible    xpath=//span[@class='oxd-userdropdown-tab']    10s
    Click Element    xpath=//span[@class='oxd-userdropdown-tab']

    # logout (FIXED)
    Wait Until Element Is Visible    xpath=//a[text()='Logout']    5s
    Click Element    xpath=//a[text()='Logout']
