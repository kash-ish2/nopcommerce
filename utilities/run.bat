@echo off

echo ===============================
echo Automation Test Execution Started
echo ===============================

cd /d C:\Users\Kashish\AutomationProject

echo Activating Virtual Environment...
call venv\Scripts\activate

echo Running Pytest Automation...
pytest -v -s --html=Reports/report.html --self-contained-html

echo ===============================
echo Test Execution Completed
echo ===============================

pause