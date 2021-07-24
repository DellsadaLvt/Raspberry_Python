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



 #!/usr/bin/python3

import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5150
server.bind((host, port))
server.listen(5)
print('Listening for a client…')
client, addr = server.accept()
print('Accepted connection from:', addr)
client.send(str.encode('Welcome to my server!'))
while True:
    data = client.recv(1024)
    if (bytes.decode(data) == 'exit'):
        break
    else:
        print('Received data from client:', bytes.decode(data))
        client.send(data)
print('Ending the connection')
client.send(str.encode('exit'))
client.close()


