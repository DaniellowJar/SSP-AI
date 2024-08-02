import subprocess
import deepl
import time
auth_key = "cbb756b2-0b71-49d0-86d1-93766110bdab:fx"
translator = deepl.Translator(auth_key)

with open("userCZ.txt", "r", encoding='utf-8') as userOutput:
    text_to_translate = userOutput.read()
print(userOutput)
enUserMessage = str(translator.translate_text(text_to_translate, target_lang="EN-US"))

with open("userEN.txt" , "w", encoding="utf-8") as userMessageEN:
    userMessageEN.write(enUserMessage)
print(userMessageEN)
def run_powershell_command(command, args):
    """
    Run a PowerShell command and capture the output.

    Args:
        command (str): The PowerShell command to run.
        *args (str): Additional arguments to pass to the command.

    Returns:
        str: The output of the PowerShell command.
    """
    # Create a subprocess to run the PowerShell command
    process = subprocess.Popen(['powershell.exe', '-Command', command] + list(args),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=False,
                               creationflags=subprocess.CREATE_NO_WINDOW)

    # Wait for the subprocess to finish and capture the output
    output, error = process.communicate()

    # Return the output as a string
    return output.decode('latin1')

# Example usage:
command = "ollama run SSPS"
with open("userEN.txt" , "r", encoding="utf-8") as userMessage:
    args = userMessage.read()

output = run_powershell_command(command, args) 
# try args:except("failed to get console mode for stderr: NeplatnÃ½ popisovaÄ.")
# print(output)


# Remove unwanted lines from the output
output = output.replace("failed to get console mode for stdout: NeplatnÃ½ popisovaÄ.\n", "")
output = output.replace("failed to get console mode for stderr: NeplatnÃ½ popisovaÄ.\n", "")

# Write the filtered output to the file
with open("AIen.txt", "w", encoding="utf-8") as output_file:
    output_file.write(output)

with open("AIen.txt", "r", encoding='utf-8') as messageToAnswer:
    messsageNTranslated = messageToAnswer.read()

czAIOutput = str(translator.translate_text(messsageNTranslated, target_lang="CS"))

with open("AIcz.txt" , "w", encoding="utf-8") as aiMessageCZ:
    aiMessageCZ.write(czAIOutput)

with open("log.txt", "r", encoding='utf-8') as LogFileR:
    logs = LogFileR.read()
    with open("log.txt", "w", encoding='utf-8') as logFileW:
        logFileW.write(logs + "\n" + "SSPS BOT : " + str(czAIOutput) + "\n \n")