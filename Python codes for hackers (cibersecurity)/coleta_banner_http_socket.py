#!/usr/bin/env python3

import socket

alvo = input("Digite o endereço eletrônico do alvo: ")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((alvo, 80))
mysock.send(b"HEAD / HTTP/1.1\r\nHost:{alvo}\r\n\r\n")

while True:
	data = mysock.recv(512)
	if len(data) < 1:
		break
	print(data)
mysock.close()
