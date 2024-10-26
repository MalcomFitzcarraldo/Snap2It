# Snap2It
 Introducing Snap2It, your all-in-one solution for effortlessly converting window captures into searchable text!

 
Installation Steps:
1. Run setup.bat
2. Follow the instructions in the setup
3. Navigate to C:\snap2it and open Snap2It.bat



Manual Setup:
1. Copy Snap2It scripts to C:\snap2it
2. Open Command Prompt as administrator.
3. Install Python (with PIP) - https://www.python.org/downloads/
4. Once installed, confirm that you have installed by typing pip --version in Command Prompt.
5. Next, install Tesseract-OCR - https://github.com/UB-Mannheim/tesseract/wiki
6. Once installed, confirm that tesseract.exe is visible in C:\Program Files\Tesseract-OCR
7. Open a new Command Prompt and type the following commands:
pip install pillow colorama pyperclip pytesseract keyboard subprocess


Ollama Setup:

INSTALL AND SETUP OLLAMA - https://ollama.com/download
1. Open API_ollama in notepad
2. Line 9 contains "model='gemma2:9b'" Replace "gemma2:9b" with the model you have loaded to ollama
3. Activate ollama for Snap2it in lines 43-47 of ocr.py.

Default ollama server address: localhost:11434
