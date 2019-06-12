from socket import * 

HOST = 'localhost'
PORT = 5215
ADDR = (HOST, PORT)

while True:
    tcpCli = socket(AF_INET, SOCK_STREAM)
    tcpCli.connect(ADDR)
    data = input('>>')
    if not data : break
    data = '%s\r\n'%data
    tcpCli.sendall(data.encode('utf-8'))
    data = tcpCli.recv(1024)
    print(data.strip())
tcpCli.close()
