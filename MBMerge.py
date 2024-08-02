import deepl
import subprocess
import time

# DeepL API settings
auth_key = "cbb756b2-0b71-49d0-86d1-93766110bdab:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

# Read the content of the input file
with open("input.txt", "r", encoding="utf-8") as input_file:
    text_to_translate = input_file.read()

# Translate the text
result = translator.translate_text(text_to_translate, target_lang="EN-US")
time.sleep(1)

# Prepare the translated text for output
translated_text = ""
if isinstance(result, list):
    for translation in result:
        translated_text += translation.text + "\n"  # Append each translation with a newline
else:
    translated_text = result.text

# Save the translated text to output.txt
with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(translated_text)

# Run PowerShell command to paste the translated text into a window
def run_powershell_command(file_path):
    command = f"Get-Content -Path '{file_path}' | Set-Clipboard; Start-Process -FilePath 'notepad.exe' -ArgumentList '/p'"
    subprocess.run(["powershell.exe", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Specify the file path
file_path = 'output.txt'

run_powershell_command(file_path)