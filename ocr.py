from PIL import Image, ImageGrab
import pytesseract
import pyperclip
import subprocess
from colorama import Fore, Style, Back

# Load the image
image = Image.open("C:/snap2it/capture.PNG")

# Recognize text from the image -- ***PATH FOR TESSERACT***
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(image)

# Save the text to a file
with open("C:/snap2it/output.txt", "w") as f:
    f.write(text)
print(Fore.CYAN + "Text extracted and saved to output.txt")
print(Style.RESET_ALL)

# Path to the text output file
filepath = 'C:/snap2it/output.txt'

# Read the content of the text file
with open(filepath, 'r') as file:
    text = file.read()

# Read the content of the file
file_path = r'C:\snap2it\output.txt'
with open(file_path, 'r') as file:
    file_content = file.read()
print(Style.DIM + file_content)
print(Style.RESET_ALL)

# Copy the text to the clipboard
pyperclip.copy(text)
print(Style.BRIGHT)
print(Fore.GREEN + "Text copied to clipboard.")
print(Style.RESET_ALL)

#OLLAMA
# Remove the "#" below to activate ollama

#subprocess.run(["python", "C:/snap2it/ai_prompt.py"])
