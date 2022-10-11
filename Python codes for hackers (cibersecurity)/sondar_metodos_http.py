#!/usr/bin/env python3

import requests

host = input("Digite o endereço eletrônico do site-alvo: " )
metodos = ["GET", "POST", "OPTIONS", "PUT", "DELETE", "TRACE", "CONNECT", "HEAD", "PATCH"]

for metodo in metodos:
	resposta = requests.request(metodo, host)
	print(metodo + " |--> " + resposta.reason)
