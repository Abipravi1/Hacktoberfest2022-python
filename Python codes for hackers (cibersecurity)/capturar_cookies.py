#!/usr/bin/env python3

import requests

session = requests.Session()
site = input("Alvo: ")
alvo = f"https://{site}"
response = session.get(alvo)
print(session.cookies.get_dict())
