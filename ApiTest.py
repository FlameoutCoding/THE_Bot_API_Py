from BotBase import BotBase

class MyTest(BotBase):
    def __init__(self,url,port,token):
        BotBase.__init__(self,url,port,token)
    def iNeedToDoSomething(self,currentAmount,currentHighestBet):
        self.fold()

botInstance = MyTest("flameout-coding.de",28001,"monika")
botInstance.authenticate()
