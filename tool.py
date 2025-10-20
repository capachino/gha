import subprocess

# Get untrusted input from a user
hostname = input("Please enter the hostname to ping: ")

# VULNERABLE: Building a command string and using shell=True
# The f-string directly inserts the user's text into the command.
command = f"ping -c 3 {hostname}"

print(f"--- Running command: {command} ---")

# shell=True tells Python to pass the entire string to the system's shell 
# (like /bin/sh or cmd.exe) to be interpreted.
try:
    subprocess.run(command, shell=True, check=True)
