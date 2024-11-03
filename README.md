# Snap2It
Introducing Snap2It, This powerful tool seamlessly captures window content, converts it to editable text using cutting-edge OCR, and even integrates with AI for advanced search capabilities.

### How it Works:
1. Capture: Capture any window instantly with a simple key press and send the image directly to your clipboard.
2. Convert: Snap2It leverages advanced OCR technology to transform the captured image in your clipboard into clear, editable text.
3. Copy: The extracted text is automatically copied back to your clipboard, ready for pasting into documents, emails, or any other application.
But that's not all!
### With Snap2It, you can unlock even deeper insights by integrating it with powerful AI tools like Ollama:
Harness the power of AI to search through the captured text directly. Find specific keywords, phrases, or concepts within your screenshots with lightning speed and accuracy.
Unlock Hidden Information: Go beyond basic keyword searches. Use Ollama's advanced capabilities to analyze the context of your screenshots, uncover hidden patterns, and gain a deeper understanding of the information presented.

![snap2it](https://github.com/user-attachments/assets/2d75f567-59db-48b4-a868-147cfb0c9746)

## Installation Steps:

1. Download and extract Snap2It, right-click in the extracted folder and click "Open in Terminal".
   
2. Create the Snap2It directory.
> [!IMPORTANT]
> Without modification, this must to be installed/run from "C:\snap2it".

   ```cmd
   mkdir "C:\snap2it"
   ```
3. Copy the Snap2It files to C:\snap2it
   ```cmd
   xcopy . "C:\snap2it\" /E /H /C /I
   ```
   
4. Install Python (with PIP) - https://www.python.org/downloads/
   - Once installed, confirm that you have installed by typing `pip --version` in the Command Prompt.

5. Run the commands below to install all the necessary Python modules:
```
pip install pillow
```
```
pip install colorama
```
```
pip install pyperclip
```
```
pip install pytesseract
```
```
pip install keyboard
```
```
pip install subprocess
```


6. Install Tesseract-OCR - https://github.com/UB-Mannheim/tesseract/wiki
   
7. Confirm that `tesseract.exe` is visible in `**C:\Program Files\Tesseract-OCR**`
   
8. Run the following code in cmd **(as admin)** to create a **desktop shortcut**: 
- Windows (Standard)
```cmd
cmd /k mklink "C:\Users\%USERNAME%\Desktop\Snap2It.lnk" "C:\snap2it\Snap2It.bat"
```
- Windows (OneDrive)
```cmd
cmd /k mklink "C:\Users\%USERNAME%\OneDrive\Desktop\Snap2It.lnk" "C:\snap2it\Snap2It.bat"
```
or Navigate to **C:\snap2it** and open Snap2It.bat


## Ollama Setup:
1. INSTALL AND SETUP OLLAMA. - https://ollama.com/download
2. Install ollama for Python.
   ```
   pip install ollama
   ```
3. Open API_ollama in notepad
4. Line 9 contains "model='`gemma2:9b`'" **Replace "gemma2:9b"* with the model you have loaded to ollama
5. Activate ollama for Snap2it in lines 43-47 of ocr.py.
6. Edit ai_prompt.txt to change the text in front of the captured text
   - Default prompt is: Find the question in the text below and give a simple answer:
   - Default ollama server address: localhost:11434
  
# Screenshots

   ![image](https://github.com/user-attachments/assets/c50fff81-9f1f-42ae-be90-70b37ce6f605)

   ![image](https://github.com/user-attachments/assets/2949374c-07ac-46e5-be08-690087910f08)

   ![image](https://github.com/user-attachments/assets/76d9e9c5-cf6e-4de7-b3e7-faa7334e0751)![snap]
   (https://github.com/user-attachments/assets/2ce73994-3fd4-4518-a077-a853bc7eafbc)






