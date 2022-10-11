#!/usr/bin/env python3

import socket

dominio = input("Alvo: ")
brute_force = ["ns1", "ns2", "ns3", "ns4", "www", "ftp", "intranet", "mail"]

for nome in brute_force:
	dns = f"{nome}.{dominio}"
	try:
		print(f"{dns}: {socket.gethostbyname(dns)}")
	except socket.gaierror:
		pass
