#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import socket
import sys
import terminal_banner
from termcolor import colored
import os
import argparse

os.system('clear')

banner_text = ("""


 █████╗ ███████╗███╗   ██╗      ███████╗ █████╗  ██████╗ ██╗     ███████╗
██╔══██╗██╔════╝████╗  ██║      ██╔════╝██╔══██╗██╔════╝ ██║     ██╔════╝
███████║███████╗██╔██╗ ██║█████╗█████╗  ███████║██║  ███╗██║     █████╗  
██╔══██║╚════██║██║╚██╗██║╚════╝██╔══╝  ██╔══██║██║   ██║██║     ██╔══╝  
██║  ██║███████║██║ ╚████║      ███████╗██║  ██║╚██████╔╝███████╗███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝      ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                                                                         
Version 2.1

Developer: Ritik Sahni
Twitter: https://twitter.com/RitikSahni22
Instagram: https://www.instagram.com/deep.tech
""")


# Print Banner for ASN-Eagle
banner_terminal = terminal_banner.Banner(banner_text)
print (colored(banner_terminal, 'cyan'))

help = (colored('python3 ASN-Eagle.py -d domain [OPTIONS]\nOPTIONS:\n\n-i\t--ip-range\tDiscover Netblocks/IP ranges\n-o\t--output-file\tWrite output to a file\n', 'green'))

arg_parse = argparse.ArgumentParser(usage=help)
arg_parse.add_argument('-d','--domain',required=True)
arg_parse.add_argument('-i','--ip-ranges', default=False, action='store_const', const = 1)
arg_parse.add_argument('-o','--output-file')
args = arg_parse.parse_args()

# Fetch IP address of website using socket and save it to a variable
hostname = (args.domain)
try:
        ip_addr = socket.gethostbyname(hostname)
except:
        print(colored('[!] No such host found!!', 'red'))
        sys.exit()

print(colored("Fetching AS Number..\n", 'white')) 

# Extract ASN using ipinfo API.
asn_fetch = requests.get('https://ipinfo.io/'+ip_addr+'/org?token=c8bb8b5ed87127')

#fetch the desired result and store it
discovered_asn = (asn_fetch.text)

print(colored("[+] ASN Details found!!\n", 'magenta')) # Print ASN details
print(colored(discovered_asn , 'yellow')) 
access_rights = (0o755) # Defining access rights for creating output directory.

path = ("./output")

if(args.ip_ranges == 1):

	#fetch the AS Number from the previous output
	new_asn = discovered_asn.split(' ')[0]
	
	print(colored("Fetching IP ranges belonging to the AS..\n", 'white')) 
		
	try:
		result = requests.get('https://api.hackertarget.com/aslookup/?q='+new_asn) # Makes request to fetch IP RANGE LIST.
		print(colored("[+] IP ranges found!!\n", 'magenta'))
		print(result.text+'\n') 
		
	except Exception:
		print("There is something wrong.")
	

if(args.output_file != None):
		
	filename = args.output_file

	try: # Creates 'output/' directory and file to save result containing IP ranges.
		os.mkdir(path, access_rights)
		
	except OSError:
		print(colored("Output directory already exists, creating file with IP ranges!", 'green'))
		
	file = open("./output/"+filename, "w")

	try:
		if(args.ip_ranges == 1):
			file.write(result.text+'\n')		#write the result with ip ranges in the file
		else:
			file.write(discovered_asn+'\n')		#write the result without ip ranges in the file
		print (colored("\nResults saved in output/"+filename+'\n', 'blue'))
		
	except Exception:
		print (colored("Task failed! Try again!", 'red'))




