@echo off
SET TOOLS_DIR=%~dp0
SET AUT_DIR=%TOOLS_DIR%..
SET PYTHONPATH=%PYTHONPATH%;%AUT_DIR%;%AUT_DIR%/libraries
"%TOOLS_DIR%/generate_kw_doc.vbs"