#!/usr/bin/python3

import requests
import socket
import sys
import terminal_banner
from termcolor import colored
import os

os.system('clear')

banner_text = ("""
 _______  _______  __    _         _______  _______  _______  ___      _______ 
|   _   ||       ||  |  | |       |       ||   _   ||       ||   |    |       |
|  |_|  ||  _____||   |_| | ____  |    ___||  |_|  ||    ___||   |    |    ___|
|       || |_____ |       ||____| |   |___ |       ||   | __ |   |    |   |___ 
|       ||_____  ||  _    |       |    ___||       ||   ||  ||   |___ |    ___|
|   _   | _____| || | |   |       |   |___ |   _   ||   |_| ||       ||   |___ 
|__| |__||_______||_|  |__|       |_______||__| |__||_______||_______||_______|

Version 2.0

Developer: Ritik Sahni
Twitter: https://twitter.com/RitikSahni22
Instagram: https://www.instagram.com/deep.tech
""")

# Print Banner for ASN-Eagle
banner_terminal = terminal_banner.Banner(banner_text)
print (colored(banner_terminal, 'cyan'))

# Fetch IP address of website using socket and save it to a variable
hostname = input(colored("Enter hostname [e.g google.com, tesla.com]: ", 'green'))
ip_addr = socket.gethostbyname(hostname)

# Extract ASN using ipinfo API.
asn_fetch = requests.get('https://ipinfo.io/'+ip_addr+'/org?token=c8bb8b5ed87127')

print(colored("ASN Details found!!\n\n"+asn_fetch.text, 'magenta')) # Print ASN details
access_rights = (0o755) # Defining access rights for creating output directory.

prompt1 = input(colored("\n\nDo you want to scan for IP ranges from discovered ASN? (Y or N)\n", 'green')) # Prompt for IP ranges

path = ("./output")

if prompt1 == "Y": # If-elif for saving IP ranges functionality.
	try:
		discovered_asn = input(colored('Enter the discovered ASN: ', 'green'))
		result = requests.get('https://api.hackertarget.com/aslookup/?q='+discovered_asn) # Makes request to fetch IP RANGE LIST.
	except Exception:
		print("Invalid ASN!")
	filename = input(colored("\nEnter the filename for saving the results [e.g. results.txt] : ", 'blue'))
	try: # Creates 'output/' directory and file to save result containing IP ranges.
		os.mkdir(path, access_rights)
	except OSError:
		print(colored("Output directory already exists, creating file with IP ranges!", 'green'))
	file = open("./output/"+filename, "w")
	try:
		file.write(result.text)
		print (colored("\n\nResults saved in output/"+filename, 'blue'))
	except Exception:
		print (colored("Task failed! Try again!", 'red'))
elif prompt1 == "N":
	sys.exit
else:
	print (colored("Invalid input!", 'red'))