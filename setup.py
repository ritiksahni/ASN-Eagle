#!/usr/bin/env python3

from setuptools import setup

fout = open("config.py", "w")
shodanInput = input("Enter your shodan API key: ")

fout.write("shodan_api = " + '"' + shodanInput + '"' + "\n")
fout.close

setup(
	name="ASN-Eagle",
	version="1.0",
	description="Tool to search for Autonomous System Numbers.",
	url="https://github.com/ritiksahni/ASN-Eagle",
	author="Ritik Sahni",
	author_email="ritiksahni0203@gmail.com",
	license="GPL-3.0",
	install_requires=["shodan", "terminal_banner"]
)
