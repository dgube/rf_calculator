*** Settings ***

Resource            ../resources/ImportResources.robot
Suite Setup         Open Mobile Application     ${PLATFORM}
Suite Teardown      Close All Applications

Test Setup          Ensure Application Is Open  ${PLATFORM}
Test Teardown       Clear Result
Test Template       Push Buttons With Empty Result

*** Variables ***

${PLATFORM}     Android

*** Keywords ***

Push Buttons With Empty Result
    [Arguments]     ${button_text}  ${expected_result}
    Push Button     ${button_text}
    Sleep   1s
    Result Should Be    ${expected_result}




*** Test Cases ***          Button              Expected Result
Push Clear                    C                     ${EMPTY}
Push Plus                     +                     ${EMPTY}
Push Minus                    -                     ${EMPTY}
Push Multiply                 *                     ${EMPTY}
Push Divide                   /                     ${EMPTY}
Push Equals                   =                     ${EMPTY}
Push Dot                      .                        .
Push One                      1                        1
Push Two                      2                        2
Push Three                    3                        3
Push Four                     4                        4


