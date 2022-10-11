#!/usr/bin/env python3

#Este script foi desenvolvido pelo professor Afonso da Silva. Inclusive, gostaria de salientar que apenas este primeiro comentário é meu (Ednelson). As únicas modificações que fiz foram ajustar os nomes das variáveis para "snake case", tendo em vista o que é convenção em scripts python.

import os
import sys
import shutil
import subprocess
import urllib
import random



def init():

    #Toda vez que o programa inicia ele verifica se os arquivos estão perdidos pela máquina chamando o comeback
    try:
        import comeback
        comeback
    except:
        pass

    user = (os.path.expanduser("~")) #Nome do Usuário da Máquina + Caminho dos arquivos

    old_adress = user + '/Desktop/gauntlet/I/' #pasta origem
    new_adress = user + '/Desktop/gauntlet/D1/' #pasta única de destino
    finish_adress = user + '/Desktop/gauntlet/F/' #pasta destino
    #Lista de Diretórios
    new_adress_list = [user + '/Desktop/gauntlet/D1/', user + '/Desktop/gauntlet/D2/', user + '/Desktop/gauntlet/D3/', user + '/Desktop/gauntlet/D4/', user + '/Desktop/gauntlet/D4/']


    list = os.listdir(old_adress) #lista separando apenas os arquivos do caminho.



    #Essa é a Lista em que serão armazenados todos os caminhos aos quais os arquivos serão enviados
    log_list = []

    contador_controle = 0 #contador de controle
    validate = True #Controle
    memory_dirs = [] #Armazena todos os diretórios
    memory_arch = [] #Armazena o nome dos arquivos
    while (validate == True):
        #print(len(os.listdir(oldAdress)))
        if (len(os.listdir(old_adress))) != 0: #Verifica quantos arquivos temos no old_adress
            caminho_completo_old = old_adress + list[contador_controle] #variável recebe caminho + arquivo, conforme indice
            __caminho_completo_new = random.choice(new_adress_list) #variável recebe caminho + arquivo, conforme índice
            caminho_completo_new = __caminho_completo_new + list[contador_controle] #Une Diretório com Arquivo

            #Adiciona o caminho no LOG
            log_list.append(caminho_completo_new)

            shutil.move(caminho_completo_old, caminho_completo_new) #módulo 'shutil.move()' move os arquivos

            hidden_adress = __caminho_completo_new[:-1] #Retira a Barra no final do caminho
            subprocess.call('attrib +s +h "'+ hidden_adress +'"', shell=True) # deixa a pasta invísivel

            #print(caminhoCompleto_new , '-')
            #print(x, '-', list[x])  # apenas para ver como está sendo feito

            memory_dirs.append(__caminhoCompleto_new) #Adiciona na memória
            memory_arch.append(list[contador_controle]) #Adiciona na memória



        else:
            validate = False #Parada da Função
        contador_controle +=1 #Contador de controle


    #Grava o LOG
    log_file = open('C:/Users/T-Gamer/Desktop/gauntlet/log.txt', 'w')
    for cont in range(len(log_list)):
        print(cont)
        log_file_text = str(log_list[cont]) + "\n"
        log_file.writelines(log_file_text)

    p = input("Qual a sua senha? ")






    def back(): #Serve para voltar os arquivos à pasta de origem caso a senha esteja correta
        y = 0
        validate = True
        while y != (len(memory_dirs)) and validate == True: #Usa as memórias para verificação

            if (len(memory_dirs)) != 0:

                hidden_adress = memory_dirs[y][:-1] #Identifica o caminho, deletando a última / para deixar visível
                if (pw == True): #Se a senha estiver correta:
                    caminho_completo_old = memory_dirs[y] + memory_arch[y] #Une o caminho + nome do arquivo
                    caminho_completo_new = old_adress + memory_arch[y] #Faz o mesmo
                    shutil.move(caminho_completo_old, finish_adress) #Envia os arquivos para a pasta FINAL
                    subprocess.call('attrib +s -h "' + hidden_adress + '"', shell=True) #Deixa tudo visível
                else:
                    subprocess.call('attrib +s +h "' + hidden_adress + '"', shell=True) #Deixa tudo Invisível
            else:
                validate = False #Critério de parada
            y += 1
        return print("finish")





    pw = False
    if (p == '123'):
        pw = True

    else:
        pw = False

    if (pw == True):
        print("Password Success")
        subprocess.call('attrib +s -h "' + old_adress[:-1] + '"', shell=True)
        print(old_adress)
        print(old_adress[-1])
        back()
    else:
        print("F")
        subprocess.call('attrib +s +h "' + old_adress[:-1] + '"', shell=True)
        back()
        sys.exit()


init()
