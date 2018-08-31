import socket


class Server:
    def __init__(self, server_port):
        self.port = server_port
        self.socket = socket.socket()
        self.host = socket.gethostname()

    def bind(self):
        self.socket.bind((self.host, self.port))
        print('Starting server on', self.host, self.port)

    def listen(self):
        self.socket.listen(5)

        while True:
            con, adrs = self.socket.accept()
            print("Connected with ", adrs)
            con.send('Content-Type: text/html\n')
            con.send('\n')
            con.send("""
                <html>
                <body>
                <h1>OH</h1>
                </body>
                </html>
            """)

    def close(self):
        self.socket.close()


def server_start():
    myServer = Server(8080)
    myServer.bind()
    myServer.listen()


server_start()
