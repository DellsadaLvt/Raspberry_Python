import socket

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to hostname server
#host= socket.gethostbyname("localhost")
host="127.0.0.1"
print("the host address" , host)
port= 5150

server.connect((host, port))
data= server.recv(1024)
print(bytes.decode(data))
while True:
    data= input("Enter text to send: ")
    server.send(str.encode(data))
    data= server.recv(1024)
    print("Receive data: ", bytes.decode(data))
    if( bytes.decode(data) == "exit"):
        break
 
print("End the connection")
server.close()
 