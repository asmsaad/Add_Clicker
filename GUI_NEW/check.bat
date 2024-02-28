@echo off

REM Set the path to the Python interpreter
set "pythonPath=D:\GitHub\Add_Clicker\GUI_NEW\bin\Python\python.exe"

REM Set the path where you want to create the virtual environment
set "venvPath=D:\GitHub\Add_Clicker\GUI_NEW\bin\venv"

REM Check if the virtual environment directory already exists
if not exist "%venvPath%" (
    echo Creating Virtual Environment ...
    "%pythonPath%" -m venv venv
    echo Virtual Environment created at %venvPath%

	REM Activate the virtual environment
	call "venv\Scripts\activate"




	REM Now, install the requirements from requirements.txt
	echo Installing requirements...
	cd bin
	pip install -r requirements.txt
	

	REM Run main.py
	echo Running main.py...
	python main.py

	
) else (
    echo Virtual Environment already exists at %venvPath%
	REM Activate the virtual environment
	call "venv\Scripts\activate"
	cd bin
	REM Run main.py
	echo Running main.py...
	python main.py

)










pause
