#!/usr/bin/env python3

import socket

host = input("Alvo: ")
portas = [22,80,443,53,21,23,8080]

for porta in portas:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	resultado = sock.connect_ex((host, porta))
	sock.close()
	if resultado == 0:
		print(porta)
