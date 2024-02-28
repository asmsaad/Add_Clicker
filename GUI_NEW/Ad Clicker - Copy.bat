@echo off

echo Current directory >> %CD%
@REM REM Virtual Environment Path
set "venvPath=.\bin\venv"

if not exist "%venvPath%" (
    echo Creating Virtual Environment ...
    cd bin
    echo Current directory >> %CD%
    Python\python.exe -m venv venv
    @REM cd venv\Scripts
    @REM activate
    @REM cd ..\..
    @REM echo Installing necessary packages ...
    @REM python -m pip install -r requirements.txt
    @REM cd ..
)

@REM echo Opening application ...
@REM cd bin
@REM python main.py

pause
