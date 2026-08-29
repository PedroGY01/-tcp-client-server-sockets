from socket import *
import sys
from pathlib import Path

if len(sys.argv) >= 3:
    server_name = sys.argv[1]
    server_port = int(sys.argv[2])

socket_server = socket(AF_INET, SOCK_STREAM) #esse socket é para ficar ouvindo
socket_server.bind((server_name, server_port))
socket_server.listen(1)

while(1):

   socket_connection, addr = socket_server.accept() #Fica bloqueado aqui até alguém se conectar
   buffer = b"" #byte type

   while b"\n" not in buffer:
      chunk = socket_connection.recv(1024)
      if (not chunk): #Só entra aqui se não recebeu nada do outro lado
        break
      buffer += chunk

   if b"\n" not in buffer:
      print("Incomplete message received")
      socket_connection.close()
      continue

   message_bytes, _, _, = buffer.partition(b"\n")
   _, _, file_name_bytes = message_bytes.partition(b" ")
   file_name = file_name_bytes.decode(encoding='UTF-8', errors='strict') # bytes to string 
   
   FILES_DIRECTORY = Path("server_files")
   file_path = FILES_DIRECTORY/file_name

   if file_path.exists():
     code = '1'
     code = code.encode("utf-8")
     socket_connection.sendall(code)
     with open(file_path, "rb") as file:
       while True:
        chunk = file.read(4096)

        if not chunk:
            break

        socket_connection.sendall(chunk)
   else:
    code = '0'
    code = code.encode("utf-8")
    socket_connection.sendall(code)
    

   socket_connection.close()