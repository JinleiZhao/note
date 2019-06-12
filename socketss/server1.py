from socket import *
from time import ctime

HOST = ''  #绑定主机
PORT = 21453 #绑定端口
BUFSIZE = 1024  #缓冲区大小
ADDR = (HOST, PORT) #


tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)  #5在连接被转接或拒绝之前，传入连接请求的最大数

while True:
    print("waiting for connecting ....")
    tcpCliSock, addr = tcpServSock.accept()  #被动接受客户端连接，客户端套接字和地址，空出主线（服务端套接字），使其可以继续监听客户端连接
    print('connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE) #接受tcp消息
        if not data:
            break   #如果消息是空的，跳出次循环，等待/进入下个客户端连接
        str_data = '[%s]%s'%(ctime(),data.decode('utf-8'))
        tcpCliSock.send(str_data.encode('utf-8'))#py3需要转化为字节
    tcpCliSock.close()
tcpServSock.close()