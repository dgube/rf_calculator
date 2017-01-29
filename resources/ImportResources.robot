*** Settings ***

#     Import variables files
Variables    ../resources/Variables.py

#    Import RF internal libraries
Library    Collections
Library    Dialogs
Library    OperatingSystem
Library    Process
Library    Screenshot
Library    String

#    Import RF external libraries
Library    AppiumLibrary    ${APPIUM_DEFAULT_TIMEOUT}    AppiumLibrary.Capture Page Screenshot

#    Import Mobile Library
Library    MobileLibrary