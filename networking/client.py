import socket



class network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        self.server = '192.168.1.108'
        self.port = 5555
        self.addr = (self.server , self.port)
        self.pos = self.connect()
    def Pos(slef):
        return self.pos
    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(1500).decode()
    def traffic(self,data):
        self.client.send(str.encode(data ))
        return self.client.recv(1500).decode()
a = network()