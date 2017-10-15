@echo on

@IF [%~1] == [] (
@ECHO "Log level not provided, loglevels: INFO/DEBUG/TRACE"
@ECHO "SYNTAX: suite_runner.bat <loglevel> <suite.txt>"
@ECHO "Example: suite_runner.bat DEBUG my_suite.txt"
@EXIT /b)
@IF [%~2] == [] (
@ECHO "Test suite not provided!"
@ECHO "SYNTAX: suite_runner.bat <loglevel> <suite.txt>"
@ECHO "Example: suite_runner.bat DEBUG my_suite.txt"
@EXIT /b)

@echo off
SET LOG_LEVEL=%1
SET TEST_SUITE=%2
SET CURRENT_FOLDER=%cd%
SET ROOT_FOLDER=%~dp0

:: we add /lib folder to the PYTHONPATH
:: this way libraries can be imported using
:: their name and not only the absolute path
SET PYTHONPATH=%PYTHONPATH%;C:\Python27\Lib\site-packages\robot;%ROOT_FOLDER%\libraries
cd %ROOT_FOLDER%
CALL robot --listener Listener --debugfile debug.txt --outputdir log --loglevel %LOG_LEVEL% %TEST_SUITE%

if %ERRORLEVEL% EQU 0 (
   echo PASS
   cd %CURRENT_FOLDER%
) else (
   echo FAIL
   cd %CURRENT_FOLDER%
   exit /b %errorlevel%
)
