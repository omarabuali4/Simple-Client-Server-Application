from socket import *
servername = '127.0.0.1'
serverport = 44444
clienSocket = socket(AF_INET, SOCK_STREAM)
clienSocket.connect((servername, serverport))
w = True
while x==True:
    message = input('enter some texts: ')
    clienSocket.send(message.encode())
    modifiedMessage = clienSocket.recv(1024)
    if modifiedMessage.decode() == '@':
        w = False
    print("from server: " , modifiedMessage.decode())
clienSocket.close()