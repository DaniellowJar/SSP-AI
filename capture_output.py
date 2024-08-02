import subprocess

# Command to run
command = ["ollama", "run", "phi3"]

# File path for output
output_file = r"C:\Users\danie\Desktop\output.txt"

try:
    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    
    # Write the output to a file
    with open(output_file, 'w') as file:
        file.write(result.stdout)
        
    print(f"Output saved to {output_file}")

except subprocess.CalledProcessError as e:
    print(f"Error running command: {e}")

except FileNotFoundError as e:
    print(f"File or directory not found: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    