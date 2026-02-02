*** Settings ***
Library   RequestsLibrary

*** Variables ***
${baseurl}  http://127.0.0.1:5000

*** Test Cases ***
Verify Get_User
    Create Session    mysession    ${baseurl}
    ${response}=      GET On Session    mysession    /users
    Status Should Be    200    ${response}
    Log    ${response.content}