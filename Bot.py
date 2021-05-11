import socket

class bot:
    s=socket.socket()
    host=''
    port=5556
    c=socket.socket
    def __init__(self):
        self.s.bind((self.host,self.port))
        self.s.listen(10)
        self.c,addr=self.s.accept()
        self.c.send(str.encode('Owner is offline..'))
        self.listen()

    def listen(self):
        while True:
            txt=str(self.c.recv(1024))
            #regression
            self.c.send(str.encode('Bot is still learning..'))

app=bot()
        
            
        
    
