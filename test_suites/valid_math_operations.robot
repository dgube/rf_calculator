*** Settings ***

Resource        ../resources/ImportResources.robot
Suite Setup      Open Mobile Application  ${PLATFORM}
Suite Teardown   Close All Applications

Test Setup          Ensure Application Is Open  ${PLATFORM}
Test Teardown       Clear Result

Test Template       Do Simple Math

*** Variables ***

${PLATFORM}     Android



*** Test Cases ***          Expression
Addition                    1+5
Subtraction                 20-7
Multiplication              3*5
Division                    14/2
