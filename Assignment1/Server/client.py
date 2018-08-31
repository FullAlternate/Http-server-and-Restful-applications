import socket


class Client:
    def __init__(self, port):
        self.socket = socket.socket()
        self.host = socket.gethostname()
        self.port = port

    def connect(self):
        self.socket.connect((self.host, self.port))
        print(self.socket.recv(1024))
        self.socket.close()

def create_client():
    theClient = Client(8080)
    theClient.connect()


create_client()

