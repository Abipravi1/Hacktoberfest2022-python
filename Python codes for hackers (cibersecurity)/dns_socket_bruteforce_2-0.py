#!/usr/bin/env python3

import socket

dominio = input("Alvo: ")
with open("bruteforce.txt", "r") as arquivo:
	brute_force = arquivo.readlines()

for nome in brute_force:
	dns = nome.strip("\n") + "." + dominio
	try:
		print(f"{dns}: {socket.gethostbyname(dns)}")
	except socket.gaierror:
		pass
