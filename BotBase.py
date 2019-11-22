import socket

class BotBase:
    def __init__(self,host,port,token):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect(host,port)
        self.authToken = token

    def authenticate(self,goIntoReadLoop=True):
        self.socket.send("{\"identifier\":\""+self.authToken+"\"}")
        if goIntoReadLoop:
            self.readLoop()

    def readLoop(self):
        buffer = ""
        while 1:
            data = self.socket.recv(1024)
            buffer += str(data)
            while "\n" in buffer:
                message = buffer[:"\n" in buffer]
                self.processMessage(message)
                message = message["\n" in buffer+1:]

    def processMessage(self,message):
        print "I got a message: "+message
