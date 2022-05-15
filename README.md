# Multi-SSH Handler
Execute a set of commands on multiple SSH enabled devices.

## Table of Contents
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Modules](#modules)
* [Running the Application Locally](#running-the-application-locally)
* [Usage](#usage)

## Getting Started
This program utilises environment variables located in an .env file in the root directory. This file should contain the following lines:
````
USER=USERNAMEHERE
PASSWORD=PASSWORDHERE
PORT=PORTNUMBERHERE
````

To change the devices that you are connecting to change add/remove IP addresses from the ip.py file located in /data.
````
ip_list = [
    "127.0.0.1",
    "192.168.0.5",
    "192.168.0.11",
    "192.168.0.2",
    "192.168.0.15"
]
````

### Prerequisites
* [Python](https://www.python.org/downloads/)

### Modules
````
# paramiko
pip install paramiko

# python-dotenv
pip install python-dotenv
````

### Running the Application Locally
````
# Run the program.
python main.py
````

## Usage
This program is useful for doing repetitive tasks on SSH enabled devices. For example, you may want to update
the banner on a dozen switches.

Keep in mind that each time the program is run the commands are executed
on all devices in the IP list - so the commands should not be device specific.
Ideally, you would ensure that all IPs correspond to devices on the same operating system
e.g. Cisco IOS. Additionally, they all need to use the same port for SSH.
This is also the case for the username and password - all devices must share the same credentials.

> **Note #1:** This program cannot handle multi-factor authentication (MFA) enabled devices.

> **Note #2:** Input is case-sensitive.
