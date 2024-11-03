from colorama import Fore, Style, Back
import subprocess
file1_path = r'C:\snap2it\ai_prompt.txt'
file2_path = r'C:\snap2it\output.txt'
output_file_path = r'C:\snap2it\ai_output.txt'
with open(file1_path, 'r') as file1:
    file1_content = file1.read()
with open(file2_path, 'r') as file2:
    file2_content = file2.read()
with open(output_file_path, 'w') as output_file:
    output_file.write(file1_content + "\n" + file2_content)

print(Back.BLUE)
print(Style.BRIGHT)
print(Fore.WHITE + "Ollama Response:")
print(Style.RESET_ALL)
subprocess.run(["python", "C:/snap2it/API_ollama.py"])
