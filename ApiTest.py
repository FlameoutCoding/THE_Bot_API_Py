from BotBase import BotBase

class MyTest(BotBase):
	def __init__(self,url,port,token):
		BotBase.__init__(self,url,port,token)
	def gotMyCards(self,card1,card2):
		pass

botInstance = MyTest("flameout-coding.de",28001,"monika")
botInstance.authenticate()
