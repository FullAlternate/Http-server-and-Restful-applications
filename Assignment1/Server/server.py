import socketserver


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        self.rData = self.request.recv(1024).decode("utf-8")
        print("Connected to {}".format(self.client_address))

        self.string_list = self.rData.split(" ")

        self.method = self.string_list[0]
        self.rFile = self.string_list[1]

        print("Client is requesting: ", self.rFile)

        self.theFile = self.rFile.split("?")[0]

        self.theFile = self.theFile.lstrip("/")
        if self.theFile == "/":
            self.theFile = "index.html"

        sFile = open(self.theFile, 'rb')
        sFile_data = sFile.read()
        sFile.close()

        header = 'HTTP/1.1 200 OK\n'

        if self.theFile.endswith(".jpg"):
            mimetype = "image/jpg"

        elif self.theFile.endswith(".css"):
            mimetype = "text/css"

        else:
            mimetype = "text/html"
        #self.request.send(index_data.encode())

        header += "Content-Type: "+str(mimetype)+"\n\n"

        response = header.encode("utf-8")
        response += sFile_data

        self.request.send(response)


class Server:
    def __init__(self, port):
        self.HOST = "localhost"
        self.PORT = port

    def create(self):
        self.server = socketserver.TCPServer((self.HOST, self.PORT), TCPHandler)

    def start(self):
        self.server.serve_forever()


if __name__ == "__main__":
    theServer = Server(8080)
    theServer.create()

    theServer.start()

