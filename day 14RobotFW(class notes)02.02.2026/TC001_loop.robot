*** Test Cases ***
Print Names using for loop
    FOR    ${Name}    IN    Ram    Ravi    Taj
        Log To Console    ${Name}
    END
*** Test Cases ***
Print Numbers using while loop
    ${count} =    Set Variable    1
    WHILE    ${count} <= 5
        Log To Console    ${count}
        ${count} =    Evaluate    ${count} + 1
    END