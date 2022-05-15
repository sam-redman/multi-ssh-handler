# ---------------------------------- MODULES ---------------------------------- #

import os
import paramiko
from dotenv import load_dotenv

from data.ip import ip_list

# -------------------------- MISC -------------------------- #

# Load the .env file.
load_dotenv()

# Setup for paramiko client.
client = paramiko.SSHClient()
client.load_system_host_keys()

# ---------------------------------- MAIN ---------------------------------- #


def run_command(command):
    """Executes a command that is given as a parameter."""

    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout:
        print('... ' + line.strip('\n'))
    return True


# List to store user commands.
command_list = []

# Capture commands from user input.
while True:
    command = input("Enter your commands one at a time (type 'exit' to execute): ")
    command_list.append(command)
    # Break out of while loop and execute commands.
    if command == "exit":
        break
    # Remove all commands from the list and break out from the while loop.
    if command == "abort":
        command_list = None
        break

# ---------------------------------- SSH/COMMAND EXECUTION ---------------------------------- #

for ip in ip_list:
    # Connect via SSH.
    client.connect(hostname=ip, username=os.environ['USER'], password=os.environ['PASSWORD'], port=os.environ['PORT'])

    # For each command that the user inputs, run them in on the device.
    for command in command_list:
        print(f"{ip}: {command}")
        run_command(command)

    # Close the connection.
    client.close()
