#coding=utf-8
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
'''
服务端
1、创建套接字：地址家族AF_UNIX/AF_INET等，套接字类型(有链接tcp)SOCK_STREAM，(无连接udp)SOCK_DGRAM
2、绑定套接字  bind
3、监听客户端（设置最大默认连接数）listen()
4、循环（等带客户端的连接）
5、被动接受客户端连接accept(),获得客户端套接字释放服务端台套接字
6、获取客户端消息（循环）
7、获取消息recv(buffsize)，py3获取的数据需要解码
8、发送服务端消息send() ,py3需要编码
9、关闭客户端套接字
客户端：
1、创建套接字 
2、主动打开连接connect(())
[循环：多次发消息]
3、发送消息send
4、接受服务端消息recv(buffsize)
5、关闭客户端套接字
'''