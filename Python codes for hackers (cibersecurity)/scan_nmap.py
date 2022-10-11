#!/usr/bin/env python3

import nmap

nmap_scan = nmap.PortScanner()

nmap_scan.scan("ufal.br", "21-80")

for host in nmap_scan.all_hosts():
	print(f"Host: {host} {nmap_scan[host].hostname()}")
	print(f"State: {nmap_scan[host].state()}")
	for proto in nmap_scan[host].all_protocols():
		print("-" * 30)
		print(f"Protocol: {proto}")

		lport = nmap_scan[host][proto].keys()
		for port in lport:
			print(f"port: {port}\tstate: {nmap_scan[host][proto][port]['state']}")
