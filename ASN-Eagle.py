#!/usr/bin/env python3

import shodan
import socket
import sys
import terminal_banner

banner_text = ("""

 _______  _______  __    _         _______  _______  _______  ___      _______ 
|   _   ||       ||  |  | |       |       ||   _   ||       ||   |    |       |
|  |_|  ||  _____||   |_| | ____  |    ___||  |_|  ||    ___||   |    |    ___|
|       || |_____ |       ||____| |   |___ |       ||   | __ |   |    |   |___ 
|       ||_____  ||  _    |       |    ___||       ||   ||  ||   |___ |    ___|
|   _   | _____| || | |   |       |   |___ |   _   ||   |_| ||       ||   |___ 
|__| |__||_______||_|  |__|       |_______||__| |__||_______||_______||_______|


Developer: Ritik Sahni
Twitter: https://twitter.com/RitikSahni22
Instagram: https://www.instagram.com/deep.tech
""")

banner_terminal = terminal_banner.Banner(banner_text)
print(banner_terminal)

try:
	from config import shodan_api
except ImportError:
	print("Please run setup.py first.")
	sys.exit()


hostname = input("Enter hostname: ")


try:
	ip_addr = socket.gethostbyname(hostname)
except Exception:
	print("Please enter a valid input (e.g. google.com, facebook.com)")
	sys.exit()

print ("IP Address: " + ip_addr)

configFile = open("config.py", "r")

api = shodan.Shodan(str(shodan_api))

shodanHost = (ip_addr)

info = api.host(shodanHost)
print("ASN found!!!\n\n" + (info['asn']))