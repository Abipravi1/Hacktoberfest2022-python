#!/usr/bin/env python3

import requests
import re
import time

def pegar_email_site(site_list):
	for index in site_list:
		data_site = requests.get(index)
		return_regex = re.findall(f"[\w\.—]+@[\w\.—]+\.\w+",data_site.text)
		if return_regex:
			return(list(set(return_regex)))
		else:
			return None

sites = ["sites alvos"]

counter = 0

try:
	for site in sites:
		mails = (pegar_email_site([site]))
		if mails != "None" or mails != None:
			print(mails)
		counter += 1
except:
	print(site)
	pass
