cls
ECHO OFF
@TITLE snap2it setup
mode con: cols=51 lines=16
:BEGIN
COLOR 1F
CLS
ECHO ***************************************************
ECHO ***************************************************
ECHO **************      Main  Menu     ****************
ECHO ***************************************************
ECHO *                                                 *
ECHO *              1 - Install                        *
ECHO *              2 - Quit                           *
ECHO *                                                 *
ECHO ***************************************************
ECHO TX-3.COM   *****************************   TX-3.COM
ECHO ***************************************************
CHOICE /N /C:12 /M "TYPE A NUMBER"%1
IF ERRORLEVEL ==5 GOTO FIVE
IF ERRORLEVEL ==4 GOTO FOUR
IF ERRORLEVEL ==3 GOTO THREE
IF ERRORLEVEL ==2 GOTO TWO
IF ERRORLEVEL ==1 GOTO ONE
GOTO END
:FIVE
cls
@START C:\Users\%Username%\Documents\RON\includes\TX3-CCD.ods
PAUSE
GOTO END
:FOUR
cls

GOTO END
:THREE
cls

PAUSE
GOTO END
:TWO
cls
call deaddrop.bat
GOTO END
:ONE
cls
ECHO Install Python (with PIP)
ECHO https://www.python.org/downloads/
ECHO Confirm once you have installed. 
PAUSE
CLS
ECHO Install Tesseract (Windows)
ECHO https://github.com/UB-Mannheim/tesseract/wiki
ECHO Confirm once you have installed.
ECHO tesseract.exe should be seen in C:\Program Files\Tesseract-OCR
PAUSE
CLS
ECHO Install ollama (OPTIONAL)
echo https://ollama.com/download
echo Once installed, open ocr.py in notepad and modify where it says to.
ECHO Confirm once you have installed/skippied. 
PAUSE
CLS
ECHO The following Python Modules are required.
ECHO pillow, colorama, pyperclip, pytesseract, keyboard, subprocess, ollama (optional)
ECHO Do you want to let the setup attempt to install now?
set /p choice="Do you want to install? (y/n): "
if /i "%choice%"=="y" (
    echo You chose to continue.
start preq.bat
    pause
) else if /i "%choice%"=="n" (
    echo You chose not to continue.
   ) else (
    echo Invalid choice. Please enter y or n.
)
cls
echo FINAL STEP!
ECHO Press any key to clean up
echo IMPORTANT: Installed to C:\snap2it
pause
mkdir "C:\snap2it"
move "%~dp0*" "C:\snap2it"
echo Installed Snap2It to C:\snap2it
echo COMPLETE
pause
cls
if /i "%choice%"=="y" (
    echo You chose to continue.
    echo MAKE SURE ALL ARE INSTALLED
START C:\snap2it\Snap2It.bat
pause
cls
) else if /i "%choice%"=="n" (
    echo You chose not to continue.
   ) else (
    echo Invalid choice. Please enter y or n.
)

:END
ECHO *
ECHO RETURNING TO MAIN MENU
ECHO *
timeout 5
GOTO BEGIN
