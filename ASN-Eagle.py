#!/usr/bin/env python3

import shodan
import socket
import sys
import terminal_banner
from termcolor import colored

banner_text = ("""
 _______  _______  __    _         _______  _______  _______  ___      _______ 
|   _   ||       ||  |  | |       |       ||   _   ||       ||   |    |       |
|  |_|  ||  _____||   |_| | ____  |    ___||  |_|  ||    ___||   |    |    ___|
|       || |_____ |       ||____| |   |___ |       ||   | __ |   |    |   |___ 
|       ||_____  ||  _    |       |    ___||       ||   ||  ||   |___ |    ___|
|   _   | _____| || | |   |       |   |___ |   _   ||   |_| ||       ||   |___ 
|__| |__||_______||_|  |__|       |_______||__| |__||_______||_______||_______|

Version 1.1

Developer: Ritik Sahni
Twitter: https://twitter.com/RitikSahni22
Instagram: https://www.instagram.com/deep.tech
""")

banner_terminal = terminal_banner.Banner(banner_text)
print (colored(banner_terminal, 'cyan'))

try:
	from config import shodan_api
except ImportError:
	print (colored("Please run setup.py first.", 'red'))
	sys.exit()


hostname = input (colored("Enter hostname: ", 'green'))

try:
	ip_addr = (socket.gethostbyname(hostname))
except Exception:
	print (colored("Please enter a valid input (e.g. google.com, facebook.com)", 'red'))
	sys.exit()

print (colored("IP Address: " + ip_addr, 'red'))
configFile = open("config.py", "r")

api = shodan.Shodan(str(shodan_api))

shodanHost = (ip_addr)

info = api.host(shodanHost)
print (colored("ASN found!!!\n\n" + (info['asn']), 'magenta'))