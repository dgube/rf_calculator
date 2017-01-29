*** Settings ***

Resource        ../resources/ImportResources.robot
Suite Setup      Open Mobile Application  ${PLATFORM}
Suite Teardown   Close All Applications

Test Setup          Ensure Application Is Open  ${PLATFORM}
Test Teardown       Clear Result

*** Variables ***

${PLATFORM}     Android

*** Test Cases ***

Result Is Updated
    Result Should Be    ${EMPTY}
    Push Button     1
    Result Should Be    1
    Push Button     1
    Result Should Be  11

Result Can Be Cleared
    Result Should Be    ${EMPTY}
    Push Button     2
    Push Button     C
    Result Should Be    ${EMPTY}





