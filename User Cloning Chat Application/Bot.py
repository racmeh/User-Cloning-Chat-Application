import socket
import training
from chatbot import ChatBot
from chatbot.trainers import ListTrainer


class bot:
    s=socket.socket()
    host='localhost'
    port=5556
    c=socket.socket
    
    chatbot=ChatBot('Bot')
    def __init__(self):
        self.train()
        self.s.bind((self.host,self.port))
        self.s.listen(10)
        self.c,addr=self.s.accept()
        self.c.send(str.encode('Owner is offline..'))
        self.listen()

    def train(self):
        trainer=ListTrainer(self.chatbot)
        fname=open("conversation.txt","r").readlines()
        trainer.train(fname)


    def listen(self):
        while True:
            text=str(self.c.recv(1024))
            x=len(text)-3
            txt=text[2:x]
            resp=str(self.chatbot.get_response(txt))+"..."
            self.c.send(str.encode(resp))
    
  
if __name__=='__main__':
    app=bot()
    
