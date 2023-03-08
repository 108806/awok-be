@echo off
@REM takeown /r /d y /f .
@REM icacls venv /grant %USERNAME% :F /

python --version
python -c "import os;print(os.__file__)"
pip install virtualenv && python -m virtualenv venv
call venv/Scripts/activate.bat
python --version
python -c "import os;print(os.__file__)"
python -m pip install -r requirements.txt
call run.bat
