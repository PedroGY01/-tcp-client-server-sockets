from socket import *
import sys

#Recebe IP/hostname (ainda não sei exatamente qual dos dois ou se tem q ser os dois)
#Recebe porta (Socket ID)
if len(sys.argv) >= 3:
    server_name = sys.argv[1]
    server_port = sys.argv[2]

#Cria um socket TCP e conecta com a porta e o servidor recebido via argumento
socket_client = socket(AF_INET, SOCK_STREAM)
socket_client.connect(server_name, server_port)

#Recebe o nome do arquivo (ainda não sei como vou tratar isso no Servidor)
file_name = input("Enter file name: ")

#Constroi a requisição, transformando a string em bytes
message = "GET" + file_name + "\n"
message_bytes = message.encode("utf-8")

#Envia os bytes
socket_client.sendall(message_bytes)

########################################################################
# Receber o arquivo de volta

socket_client.close()
