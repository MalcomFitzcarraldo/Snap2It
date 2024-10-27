@echo off
if exist "C:\snap2it" (
    Success.
START C:\snap2it\watcher.py
) else (
color C
    echo ERROR 404 - Not Installed.
    echo The Snap2It files must be in "C:\snap2it\".
pause
    
)
