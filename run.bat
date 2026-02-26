@echo off
cd /d %~dp0

echo Activating virtual environment...
call .venv\Scripts\activate

echo Running pytest...
pytest -v

pause