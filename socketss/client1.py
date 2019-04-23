from socket import * 

HOST = 'localhost'
PORT = 21453
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)  #主动打tcp服务连接

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8')) #发送数据
    data = tcpCliSock.recv(BUFFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()