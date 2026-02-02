*** Settings ***
Library    BuiltIn
Library    Collections

*** Test Cases ***
Robot Framework Control Structures Demo

    Log To Console    ==============================
    Log To Console    ROBOT FRAMEWORK CONTROL STRUCTURES
    Log To Console    ==============================

    ############################
    # IF condition
    ############################
    Log To Console    ---- IF condition ----
    ${age}=    Set Variable    20
    IF    ${age} >= 18
        Log To Console    Eligible to vote
    END

    ############################
    # IF – ELSE
    ############################
    Log To Console    ---- IF ELSE ----
    ${num}=    Set Variable    5
    IF    ${num} > 10
        Log To Console    Greater than 10
    ELSE
        Log To Console    Less than or equal to 10
    END

    ############################
    # IF – ELSE IF – ELSE
    ############################
    Log To Console    ---- IF ELSE IF ----
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log To Console    Grade A
    ELSE IF    ${marks} >= 75
        Log To Console    Grade B
    ELSE
        Log To Console    Grade C
    END

    ############################
    # Inline IF
    ############################
    Log To Console    ---- Inline IF ----
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'
        Log To Console    Test Passed
    END

    ############################
    # FOR loop (basic)
    ############################
    Log To Console    ---- FOR loop (basic) ----
    FOR    ${item}    IN    one    two    three
        Log To Console    Item: ${item}
    END

    ############################
    # FOR loop with list
    ############################
    Log To Console    ---- FOR loop with list ----
    @{COLORS}=    Create List    Red    Green    Blue
    FOR    ${color}    IN    @{COLORS}
        Log To Console    Color: ${color}
    END

    ############################
    # FOR loop – IN RANGE
    ############################
    Log To Console    ---- FOR loop IN RANGE ----
    FOR    ${i}    IN RANGE    1    6
        Log To Console    Number: ${i}
    END

    ############################
    # FOR loop – with step
    ############################
    Log To Console    ---- FOR loop with STEP ----
    FOR    ${i}    IN RANGE    0    10    2
        Log To Console    Value: ${i}
    END

    ############################
    # FOR loop – ENUMERATE
    ############################
    Log To Console    ---- FOR loop ENUMERATE ----
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log To Console    ${index} = ${value}
    END

    ############################
    # FOR loop – ZIP (SAFE)
    ############################
    Log To Console    ---- FOR loop ZIP (safe) ----
    @{USERS}=    Create List    admin    user
    @{PWDS}=     Create List    admin123    user123
    FOR    ${i}    IN RANGE    0    2
        ${u}=    Get From List    ${USERS}    ${i}
        ${p}=    Get From List    ${PWDS}     ${i}
        Log To Console    ${u} / ${p}
    END

    ############################
    # Nested FOR loop
    ############################
    Log To Console    ---- Nested FOR loop ----
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log To Console    i=${i}, j=${j}
        END
    END

    ############################
    # FOR loop with IF
    ############################
    Log To Console    ---- FOR loop with IF ----
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log To Console    Found 3
        END
    END

    ############################
    # BREAK
    ############################
    Log To Console    ---- BREAK example ----
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log To Console    ${i}
    END

    ############################
    # CONTINUE
    ############################
    Log To Console    ---- CONTINUE example ----
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log To Console    ${i}
    END

    ############################
    # WHILE loop
    ############################
    Log To Console    ---- WHILE loop ----
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log To Console    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END

    ############################
    # WHILE with BREAK
    ############################
    Log To Console    ---- WHILE with BREAK ----
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log To Console    ${i}
        ${i}=    Evaluate    ${i} + 1
    END

    ############################
    # TRY / EXCEPT / FINALLY
    ############################
    Log To Console    ---- TRY EXCEPT FINALLY ----
    TRY
        Fail    Something went wrong
    EXCEPT
        Log To Console    Error handled
    FINALLY
        Log To Console    Always executed
    END

    ############################
    # Run Keyword If
    ############################
    Log To Console    ---- Run Keyword If ----
    Run Keyword If    '${status}' == 'PASS'    Log To Console    Run Keyword If: PASS

    ############################
    # Run Keyword Unless (modern)
    ############################
    Log To Console    ---- Run Keyword Unless ----
    ${result}=    Set Variable    FAIL
    IF    '${result}' != 'PASS'
        Log To Console    Run Keyword Unless replacement: FAIL
    END

    Log To Console    ==============================
    Log To Console    EXECUTION COMPLETED SUCCESSFULLY
    Log To Console    ==============================
