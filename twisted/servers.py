from twisted.internet import protocol, reactor


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        # As soon as any data is received, write it back
        print('client said:',data)
        from time import sleep 
        sleep(5)
        data = "{'name':'Tom','age':12,'msg':'Thank You!'}".encode('utf-8') #转化成字节
        self.transport.write(data)   #发送给客户端


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

'''
@@@@@@transports
write                   以非阻塞的方式按顺序依次将数据写到物理连接上
writeSequence           将一个字符串列表写到物理连接上
loseConnection          将所有挂起的数据写入，然后关闭连接
getPeer                 取得连接中对端的地址信息
getHost                 取得连接中本端的地址信息

@@@@@protocols
makeConnection               在transport对象和服务器之间建立一条连接
connectionMade               连接建立起来后调用
dataReceived                 接收数据时调用
connectionLost               关闭连接时调用

'''

reactor.listenTCP(8000, EchoFactory())
reactor.run()
