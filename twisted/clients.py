from twisted.internet import reactor, protocol
import time

class EchoClient(protocol.Protocol):
    def sendData(self):
        # data = input('> ')
        # if data:
        #     print('sending data %s'%data)
        #     self.transport.write(data.encode('utf-8'))
        # else:
        #     self.transport.loseConnection()
        #while True:
        print('sending data')
        time.sleep(5)
        self.transport.write("hello".encode('utf-8'))

    def connectionMade(self):  # 连接建立起来后调用
        # self.transport.write("hello, world!".encode('utf-8'))  #发送给服务端
        self.sendData()
    '''
    def dataReceived(self, data):  # 接收数据时调用
        # print("Server said:", data)    #从服务端接受的数据
        # self.transport.loseConnection()
        print(data.decode('utf-8'))
        self.sendData()
    '''
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
