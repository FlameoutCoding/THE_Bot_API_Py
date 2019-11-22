import json
import socket

class BotBase:
    def __init__(self,host,port,token):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((host,port))
        self.authToken = token

    def authenticate(self,goIntoReadLoop=True):
        self.socket.send("{\"identifier\":\""+self.authToken+"\"}\n")
        if goIntoReadLoop:
            self.readLoop()

    def readLoop(self):
        buffer = ""
        while 1:
            data = self.socket.recv(1024)
            buffer += str(data)
            while "\n" in buffer:
                message = buffer[:buffer.index("\n")]
                self.processMessage(message)
                message = message[buffer.index("\n")+1:]

    def processMessage(self,message):
		parsedMessage = json.loads(message)
		if parsedMessage["response"] == "info":
			if parsedMessage["type"] == "OpenMyCards":
				card1 = int(parsedMessage["my.card0"])
				card2 = int(parsedMessage["my.card1"])
				self.gotMyCards(card1,card2)
				return
		
        print "Warn: Unparsed Message: "+message

	def gotMyCards(self,card1,card):
		print "Unhandled Action: gotMyCards (",card1,",",card2,")"
