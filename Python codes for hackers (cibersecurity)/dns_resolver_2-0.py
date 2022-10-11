#!/usr/bin/env python3

import dns.resolver

alvo = input("Alvo: ")

result = dns.resolver.resolve(alvo, "A")
for ipval in result:
	print(f"IP: {ipval.to_text()}")
	ip_alvo = ipval.to_text()

print("-" * 30)

try:
	result = dns.resolver.resolve(alvo, "CNAME")
	for cnameval in result:
		print(f"CNAME: {cnameval.target}")
except:
	pass

print("-" * 30)

try:
	result = dns.resolver.resolve(alvo, "AAAA")
	for val in result:
		print(f"AAAA: {ipval.to_text()}")
except:
	pass

print("-" * 30)

try:
	result = dns.resolver.resolve(ip_alvo+".in.addr.arpa", "PTR")
	for val in result:
		print(f"PTR: {val.to_text()}")
except:
	pass

print("-" * 30)
try:
	result = dns.resolver.resolve(alvo, "NS")
	for val in result:
		print(f"NS: {val.to_text()}")
except:
	pass

print("-" * 30)

try:
	result = dns.resolver.resolve(alvo, "MX")
	for exdata in result:
		print(f"MX: {exdata.to_text()}")
except:
	pass

print("-" * 30)

try:
	result = dns.resolver.resolve(alvo, "SOA")
	for val in result:
		print(f"SOA: {val.to_text()}")
except:
	pass

print("-" * 30)

try:
	result = dns.resolver.resolve(alvo, "TXT")
	for val in result:
		print(f"TXT: {val.to_text()}")
except:
	pass
