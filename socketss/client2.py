from socket import *

HOST = 'localhost'
PORT = 21453
BUFFSIZE = 1024

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect((HOST, PORT))

while True:
    words = input('>')
    if not words:
        break
    tcpCliSock.send(words.encode('utf-8'))
    data = tcpCliSock.recv(BUFFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()
