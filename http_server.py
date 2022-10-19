from base64 import decode
from socket import *


file = open("coen366.html", 'r',encoding='utf-8')
data = file.read()
file.close()


HOST = "172.30.107.41"
PORT = 12000
Server_Socket = socket(AF_INET, SOCK_STREAM)
# Server_Socket.close()

Server_Socket.bind((HOST,PORT))
Server_Socket.listen(1)

print("Server is currently listening")


while True:
    # Create a socket object    and return the object and a tupple of adresses
    messageobject, addr= Server_Socket.accept()
    decodedMessage = messageobject.recv(1024).decode('utf-8')
    print(f"The decode message is : {decodedMessage}" )


    messageobject.send(('HTTP/1.1 200 OK\n').encode())
    messageobject.send(('Content-Type: text/html\n\n)'.encode()))
    messageobject.send(data.encode())

    messageobject.close()
    Server_Socket.close()




# chrome ask for a file html , we get he question we parse , we check if we have it and we send it back to chrome which will output it .
