from tkinter import *
import socket
from threading import *
import nlpcontent
import training

'''
class listen (Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            app1.changeText()'''
    
class window(Frame):
    textarea=Text
    textfield=Text
    s=socket.socket()
    host='localhost'
    port=5555
    c=socket.socket
    
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        t1=Thread(target= self.threader)
        t1.start()
        t2=Thread(target=self.threader2)
        t2.start()
           
    def threader(self):
        while True:
            self.changeText()

    def threader2(self):
        self.s.bind((self.host,self.port))
        self.s.listen(10)
        self.c,addr=self.s.accept()
        
    def init_window(self):
        self.master.title("Owner")
        self.pack(fill=BOTH, expand=1)
        #textarea=Message(self, text='hello')
        self.textarea=Text(self)
        self.textarea.place(x=25, y=25, width=450, height=450)
        #textarea.insert(END, 'Can you edit me')
        self.textarea.configure(state='disabled')
        '''textarea.configure(state='normal')
        textarea.insert(END, '\nCan you still edit me')
        textarea.configure(state='disabled')'''
        self.textfield=Text(self)
        self.textfield.place(x=25, y=500, width=375, height=75)
        send=Button(self, text="Send", command=self.sendMessage) #sendMessage() will call the fn whereas sendMessage specifies the action
        send.place(x=425, y=500,width=50,height=75)
        
    def sendMessage(self):
        self.textarea.configure(state='normal')
        self.textarea.insert(END,'You: '+ self.textfield.get('1.0', END))
        self.textarea.configure(state='disabled')
        self.c.send(str.encode(self.textfield.get('1.0', END)))
        self.textfield.delete('1.0', END)

    def changeText(self):
        try:
            text=str(self.c.recv(1024))
            x=len(text)-3
            txt=text[2:x]
            self.textarea.configure(state='normal')
            self.textarea.insert(END,'User: '+ txt+'\n')
            self.textarea.configure(state='disabled')
        except Exception as e:
            i=1

    def sendAndDest(self):
        resp=self.textarea.get('1.0', END)
        print(resp)
        nlpcontent.nlpmodule(resp)
        training.train()
        Dest()

def Dest():
    root.destroy()

root=Tk()
root.geometry("500x600")
app1=window(root)
root.protocol("WM_DELETE_WINDOW", app1.sendAndDest)
root.mainloop()
