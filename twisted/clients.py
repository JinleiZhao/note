from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):  # 连接建立起来后调用
        self.transport.write("hello, world!".encode('utf-8'))  #发送给服务端

    def dataReceived(self, data):  # 接收数据时调用
        print("Server said:", data)    #从服务端接受的数据
        self.transport.loseConnection()


    def connectionLost(self, reason):
        print("connection lost")


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()


    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()


    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()


reactor.connectTCP("127.0.0.1", 8000, EchoFactory())
reactor.run()
