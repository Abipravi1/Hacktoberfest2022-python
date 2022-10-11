#!/usr/bin/env python3

import whois

dominio = input("Alvo: ")
consulta_whois = whois.whois(dominio)

print(consulta_whois.text)
