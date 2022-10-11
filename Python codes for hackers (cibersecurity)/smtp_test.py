#!/usr/bin/env python3

import socket

usuarios = ["contato","comercial","financeiro","vendas","atendimento","sac","root","trial"]
alvo = input("Alvo: ")

for usuario in usuarios:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((alvo,25))
	sock.recv(1024)
	sock.send("VRFY" + usuario + "\n")
	smtp_resultado = sock.recv(1024)
	sock.close()
	match smtp_resultado:
		case "252":
			print(f"{usuario} —> Válido!")
		case "550":
			print(f"{usuario} —> Usuário inválido!")
		case "503":
			print("Servidor requer autenticação!")
			break
		case "500":
			print("Comando VRFY não suportado pelo servidor!")
		case _:
			print(f"Resposta do servidor: {smtp_resultado}")
