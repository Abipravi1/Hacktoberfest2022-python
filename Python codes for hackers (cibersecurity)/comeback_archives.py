#!/usr/bin/env python3

# Este script foi desenvolvido pelo professor Afonso da Silva. Apenas mudei o nome da primeira variável e a deixei em "snake case".

import os
import sys
import shutil


caminho_back = 'C:/Users/T-Gamer/Desktop/gauntlet/I'
read_log_file = open('C:/Users/T-Gamer/Desktop/gauntlet/log.txt', 'r')
for i in read_log_file:
    i = i.replace("\n",'')
    shutil.move(i, caminho_back)
