#!/usr/bin/python3
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname('localhost')
port = 5150

server.connect((host, port))
data = server.recv(1024)
print(bytes.decode(data))
while True:
    data = input('Enter text to send:')
    server.send(str.encode(data))
    data = server.recv(1024)
    print('Received from server:', bytes.decode(data))
    if (bytes.decode(data) == 'exit'):
        break
print('Closing connection')
server.close()