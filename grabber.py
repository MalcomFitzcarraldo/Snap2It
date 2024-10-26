from PIL import ImageGrab
from colorama import Fore, Style
import pyperclip
import subprocess

# Get the image from the clipboard
image = ImageGrab.grabclipboard()

if isinstance(image, ImageGrab.Image.Image):
    # Save the image to a specific path
    image.save(r'C:/snap2it/capture.PNG', 'PNG')
    print(Fore.CYAN + "Image found and captured successfully.")
    subprocess.run(["python", "C:/snap2it/ocr.py"])

else:
    print(Fore.RED + "ERROR: No image found in clipboard.")


