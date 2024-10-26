from PIL import ImageGrab
import keyboard
import subprocess
import os
from colorama import Fore, Back, Style
print(Back.BLUE + "READY - WAITING FOR INPUT")
print(Style.RESET_ALL)
print(Fore.WHITE + "(Alt + Print Screen) to take a screenshot of the active window.")
print(Fore.WHITE + "(Alt + Insert) to convert to text.")

def run_ocr():
     os.system('cls')
     subprocess.run(["python", "C:/snap2it/grabber.py"])

keyboard.add_hotkey("alt+insert", run_ocr)

keyboard.wait()