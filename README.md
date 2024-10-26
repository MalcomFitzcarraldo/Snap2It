# Snap2It
Introducing Snap2It, your all-in-one solution for effortlessly converting window captures into searchable text!

### Here's how it works:
Capture: Snap any window with a simple key press and send the image directly to your clipboard.
Convert: Snap2It uses cutting-edge OCR technology to instantly transform the captured image in your clipboard into clear, editable text.
Copy: The extracted text is automatically copied back to your clipboard, ready for pasting into documents, emails, or any other application.
But that's not all!
### With Snap2It, you can unlock even deeper insights by integrating it with powerful AI tools like Ollama:
Harness the power of AI to search through the captured text directly. Find specific keywords, phrases, or concepts within your screenshots with lightning speed and accuracy.
Unlock Hidden Information: Go beyond basic keyword searches. Use Ollama's advanced capabilities to analyze the context of your screenshots, uncover hidden patterns, and gain a deeper understanding of the information presented.




 
## Installation Steps:
1. Run setup.bat
2. Follow the instructions in the setup
3. Navigate to **C:\snap2it** and open Snap2It.bat


## Manual Setup:
1. Copy Snap2It scripts to C:\snap2it
2. Open Command Prompt as administrator.
3. Install Python (with PIP) - https://www.python.org/downloads/
4. Once installed, confirm that you have installed by typing pip --version in Command Prompt.
5. Next, install Tesseract-OCR - https://github.com/UB-Mannheim/tesseract/wiki
6. Once installed, confirm that tesseract.exe is visible in **C:\Program Files\Tesseract-OCR**
7. Open a new Command Prompt and type the following commands:
`pip install pillow colorama pyperclip pytesseract keyboard subprocess`


## Ollama Setup:
INSTALL AND SETUP OLLAMA - https://ollama.com/download
1. Open API_ollama in notepad
2. Line 9 contains "model='gemma2:9b'" **Replace "gemma2:9b"*8 with the model you have loaded to ollama
3. Activate ollama for Snap2it in lines 43-47 of ocr.py.
4. Edit ai_prompt.txt to change the text in front of the captured text
   Default prompt is: Find the question in the text below and give a simple answer:
   Default ollama server address: localhost:11434


   ![image](https://github.com/user-attachments/assets/2949374c-07ac-46e5-be08-690087910f08)

   ![image](https://github.com/user-attachments/assets/76d9e9c5-cf6e-4de7-b3e7-faa7334e0751)


