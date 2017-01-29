*** Settings ***

Resource        ../resources/ImportResources.robot
Suite Setup      Open Mobile Application  ${PLATFORM}
Suite Teardown   Close All Applications

Test Setup          Ensure Application Is Open  ${PLATFORM}
Test Teardown       Clear Result

*** Variables ***

${PLATFORM}     Android
${INFINITY}     9999999999999999999999*9999999999999999999=

*** Test Cases ***

Division By Zero
    Type Expression     1/0=
    Result Should Be    Invalid operation: division by zero!

Large Numbers
    Type Expression     ${INFINITY}
    Result Should Be    Infinity

Result Should Be Cleared Automatically When New Digit Is Typed
    Type Expression     1+2=
    Result Should Be    3.0
    Type Expression     4*2=
    # the fact that int result is diplayed with one decimal
    # could be considered as a bug
    # we consider it as a feature for now
    Result Should Be    8.0

After Infnity Result Should Be Cleared When New Digit Is Typed
    Type Expression     ${INFINITY}
    Result Should Be    Infinity
    Type Expression     1+2=
    Result Should Be    3.0

Result Should Be Used As First Operand If New Operation Is Typed
    Type Expression     1+2=
    Result Should Be    3.0
    Push Button         *
    Push Button         2
    Result Should Be    6.0