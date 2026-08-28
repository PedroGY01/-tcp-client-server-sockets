from socket import *
import sys
from collections import deque

queue = deque()

#Recebe IP/hostname (ainda não sei exatamente qual dos dois ou se tem q ser os dois)
#Recebe porta (Socket ID)
if len(sys.argv) >= 3:
    server_name = sys.argv[1]
    server_port = sys.argv[2]

socket_server = socket(AF_INET, SOCK_STREAM) #esse socket é para fazer a conexão TCP, não é (no momento) o que será usado para conectar com o client side, isso pode ser mudado no futuro se for necessário 
socket_server.bind(server_name, server_port)
socket_server.listen(1) #Esse 1 é o limite de conexões que podem ficar em espera enquanto o servidor esta busy, verificar qual o valor que será necessário colocar aqui

while(1):

   socket_connection, addr = socket_server.accept() #Fica bloqueado aqui até alguém se conectar

   buffer = b"" #byte type

   while b"\n" not in buffer:
      chunk = socket_connection.recv(1024) #Quase ctz que esse valor 1024 precisa ser mudado, ver o pq

      if (not chunk): #Só entra aqui se não recebeu nada do outro lado
        break

      buffer += chunk # keep adding chunks to the buffer


   if b"\n" not in buffer:
      print("Incomplete message received or no message at all")
      socket_connection.close()
      continue

    
