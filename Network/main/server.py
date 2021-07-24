import socket

# AF_INET: IPv4 network address, SOCK_STREAM: use TCP
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen all host
host= ""
port= 5150
server.bind((host, port))
server.listen(5)

print("Listening for client\n")
client, addr= server.accept()
print("Accepted connection from: ", addr)
client.send(str.encode("welcom to my server"))

while True:
    data= client.recv(1024)
    if(bytes.decode(data)== "exit"):
        break
    else:
        print("Receive data from client: ", bytes.decode(data))
        client.send(data)

print("End of connection\n")
client.send(str.encode("exit"))
client.close()







