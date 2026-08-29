from socket import *
import sys

if len(sys.argv) >= 3:
    server_name = sys.argv[1]
    server_port = int(sys.argv[2])

#Cria um socket TCP e conecta com a porta e o servidor recebido via argumento
socket_client = socket(AF_INET, SOCK_STREAM)
socket_client.connect((server_name, server_port))

file_name = input("Enter file name: ")

#Constroi a requisição, transforma a string em bytes
message = "GET " + file_name + "\n"
message_bytes = message.encode("utf-8")

#Envia os bytes
socket_client.sendall(message_bytes)

code = socket_client.recv(1024)
code = code.decode(encoding='UTF-8', errors='strict')

if(code == '1'):
    with open(file_name, "wb") as file:
        while True:
            file_bytes = socket_client.recv(4096)

            if not file_bytes:
                break

            file.write(file_bytes)
else:
    print("0 - File not Found")

socket_client.close()
