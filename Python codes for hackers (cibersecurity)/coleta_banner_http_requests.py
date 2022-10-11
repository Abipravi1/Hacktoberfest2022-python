#!/usr/bin/env python3

import requests

host = input("Digite o alvo desejado: ")
metodos = ["GET","POST","OPTIONS","PUT","DELETE","TRACE","CONNECT","HEAD","PATCH"]

for metodo in metodos:
	resposta = requests.request(metodo, host)
	print(f"{metodo} |——> {resposta.reason}")
