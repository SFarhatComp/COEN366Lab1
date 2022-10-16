from socket import *
import threading


HOST = "192.168.56.1"
PORT = 12000
file = open("coen366.html", 'r')
data = file.read()
file.close()


Server_Socket = socket(AF_INET, SOCK_STREAM)

Server_Socket.connect((HOST, PORT))


while True:

    Server_Socket.listen(1)
    # Create a socket object    and return the object and a tupple of adresses
    messageobject, addr = Server_Socket.accept()
    decodedMessage = messageobject.recv(1024).decode()
    # if decodedMessage == data:
    messageobject.send(data.encode())
    messageobject.close()

# chrome ask for a file html , we get he question we parse , we check if we have it and we send it back to chrome which will output it .
