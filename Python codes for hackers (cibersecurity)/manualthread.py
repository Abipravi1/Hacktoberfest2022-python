#!/usr/bin/env python3

from threading import Thread
import pikepdf
from tqdm import tqdm
import time

loop = tqdm(total=999, position=0, leave=False)
start_time = time.time()

def test_pdf(pwd):
    try:
        pikepdf.Pdf.open('doc.pdf', password=str(pwd).zfill(3))
        print('Senha: '+ str(pwd).zfill(3))
        print('Tempo: '+ str(time.time() - start_time))
        exit()
    except:
        loop.update(1)
        pass

data_pwd = list(range(0,999))
counter = 0

while True:
    processThread1 = Thread(target=test_pdf, args=(data_pwd[counter],))
    processThread1.start()
    counter += 1
    processThread2 = Thread(target=test_pdf, args=(data_pwd[counter],))
    processThread2.start()
    counter += 1
    processThread3 = Thread(target=test_pdf, args=(data_pwd[counter],))
    processThread3.start()
    counter += 1
    processThread1.join()
    processThread2.join()
    processThread3.join()
