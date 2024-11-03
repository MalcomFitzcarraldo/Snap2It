from colorama import Fore, Style, Back
import subprocess
print(Style.BRIGHT)
print(Fore.WHITE)
from ollama import Client
file_path = r'C:\snap2it\ai_output.txt'
with open(file_path, 'r') as file:
    file_content = file.read().strip()
client = Client(host='http://localhost:11434')
response_stream = client.chat(model='gemma2:9b', messages=[{
    'role': 'user',
    'content': f'{file_content}',
}], stream=True)

for chunk in response_stream:
    print(chunk['message']['content'], end='')

print(Fore.RED + Back.BLACK + Style.BRIGHT + "" + Style.RESET_ALL)
print(Fore.RED + Back.BLACK + Style.BRIGHT + "Press ENTER to RESET" + Style.RESET_ALL)
print(Fore.YELLOW + Back.RED + Style.BRIGHT + "Press ENTER to RESET response and start a new snap." + Style.RESET_ALL)
print(Fore.RED + Back.BLACK + Style.BRIGHT + "Press ENTER to RESET" + Style.RESET_ALL)
input()

subprocess.run(["python", "C:/snap2it/watcher.py"])
quit()
