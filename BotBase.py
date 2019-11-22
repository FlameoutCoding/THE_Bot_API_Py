import json
import socket

class BotBase:
    def __init__(self,host,port,token): #TODO Make slot blocking
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((host,port))
        self.authToken = token
        self.myGameSlot = -1

    def authenticate(self,goIntoReadLoop=True):
        self.socket.send("{\"identifier\":\""+self.authToken+"\"}\n")
        if goIntoReadLoop:  #suboptimal solution, preferably wait for one message and only enter permanent loop after successful auth
            self.readLoop()

    def readLoop(self):
        buffer = ""
        while 1:
            data = self.socket.recv(1024)
            buffer += str(data)
            while "\n" in buffer:
                message = buffer[:buffer.index("\n")]
                self.processMessage(message)
                buffer = buffer[buffer.index("\n")+1:]

    def processMessage(self,message):
        parsedMessage = json.loads(message)
        
        if parsedMessage["response"] == "ok":
            self.authenticationSuccessful(parsedMessage["identified"])
            return
        
        if parsedMessage["response"] == "info":
            if parsedMessage["type"] == "OpenMyCards":
                card1 = int(parsedMessage["my.card0"])
                card2 = int(parsedMessage["my.card1"])
                self.gotMyCards(card1,card2)
                return
        
        if parsedMessage["response"] == "action":
            if int(parsedMessage["activePlayer"]) == self.myGameSlot:
                self.iNeedToDoSomething(int(parsedMessage["currentBet"]),int(parsedMessage["highestBet"]))
            else:
                self.enemyNeedsToDoSomething(int(parsedMessage["activePlayer"]),int(parsedMessage["currentBet"]),int(parsedMessage["highestBet"]))
            return
        
        print "Warn: Unparsed Message: "+message

    def authenticationSuccessful(self,slot):
        print "Authentication successful, slot id: ",slot
        self.myGameSlot = slot
        
    def gotMyCards(self,card1,card2):
        print "Unhandled Action: gotMyCards (",card1,",",card2,")"

    def iNeedToDoSomething(self,currentAmount,currentHighestBet):
        print "Unhandled Action: iNeedToDoSomething (",currentAmount,",",currentHighestBet,")"
        
    def enemyNeedsToDoSomething(self,slot,currentAmount,currentHighestBet):
        print "Unhandled Action: enemyNeedsToDoSomething (",slot,",",currentAmount,",",currentHighestBet,")"
