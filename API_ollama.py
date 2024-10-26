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
