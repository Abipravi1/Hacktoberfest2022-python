#!/usr/bin/env python3

# This script is from a beginner trying think about the possibilities of a trojan.
# The bash command can be one really dangerous, of course, disguised under a "normal" permission request.

import subprocess
import time
import os

with open("/tmp/invasao.sh", "w") as invasao:
	invasao.write("mkdir ~/<desktop>/<user>/<folder>/ && touch ~/<desktop>/<user>/<folder>/result.txt && echo 'A invasão foi bem-sucedida!' > ~/<desktop>/<user>/<folder>/result.txt""\n")
time.sleep(0.1)
subprocess.run(["bash","/tmp/invasao.sh"])
time.sleep(0.1)
subprocess.run(["mkdir", "programa_normal"])
time.sleep(0.1)
os.chdir("programa_normal/")
with open("instalacao_normal.txt", "w") as instalacao:
	instalacao.write("Instalação bem-sucedida!""\n")
