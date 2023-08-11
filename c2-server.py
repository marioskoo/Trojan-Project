#!/usr/bin/python3
import socket
import base64
import random
from string import ascii_lowercase

# creo TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ascolto on localhost port 1337
s.bind(("127.0.0.1", 1337))

# metto in coda fino a 5 richieste
s.listen(5)

print("listening on port 1337...")

while True:
	# stabilisco la connessione
	clientsocket, client_ip = s.accept()
	print("[+] received a connection from -> {}".format(client_ip))

	# prendo dati codificati
	encoded_data = clientsocket.recv(4096)
	clientsocket.close()

	# apro un file con un nome randomico e inserisco i dati decodificati dentro 
	random_fd = open("".join(random.choices(ascii_lowercase, k = 10)), "w")
	random_fd.write(base64.b64decode(encoded_data).decode("UTF-8"))
	random_fd.close()
