@echo off
cd /d "%~dp0"
python -c "import PyQt6" 2>nul || python -m pip install --user PyQt6
start "" pythonw -m atl_tax_deed_test
