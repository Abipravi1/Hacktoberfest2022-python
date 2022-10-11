#!/usr/bin/env python3

import dns.resolver

dominio = input("Alvo: ")
registros = ["AAAA", "A", "MX", "NS"]

for registro in registros:
	resultado = dns.resolver.query(dominio, registro, raise_on_no_answer=False)
	if resultado.rrset is not None:
		print(resultado.rrset)
