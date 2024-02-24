from socket import *

serverport = 44444
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print("iam ready! 'the server'")
connectionSocket, addr = serverSocket.accept()
d = {}
with open("ozax.txt") as f:
    for line in f:
        k1 = line.split()
        d[k1[0]] = k1 [1]
w = True
while w==True:
    sentence = connectionSocket.recv(1024)
    sentence = sentence.decode()
    if sentence == '@':
        w = False
    sentence = d[sentence]
    print('text from client: ', addr, sentence)
    connectionSocket.send(sentence.encode())
connectionSocket.close()
