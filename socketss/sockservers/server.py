from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = 'localhost'
PORT = 5215
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    
    def handle(self):  #没收到一个来自客户端的消息都会调用handle
        print('connect from :',self.client_address)
        while True:
            try:
                data = self.rfile.readline(1024)
                if not data:break
                data = '[%s] %s' %(ctime(), data.decode('utf-8'))
                self.wfile.write(data.encode('utf-8'))
            except Exception as e:
                print('e',e)
                break


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connet...')
tcpServ.serve_forever()  #循环