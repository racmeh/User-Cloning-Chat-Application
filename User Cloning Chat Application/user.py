from tkinter import *
import socket
from threading import *


'''class listen (Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            text=str(window.s.recv(1024))
            app.changeText( text)'''
                
class window(Frame):
    textarea=Text
    textfield=Text
    s=socket.socket()
    c=socket
    host='localhost'
    port=5555
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        try:
            self.c=self.s.connect((self.host, self.port))
        except Exception as e:
            self.c=self.s.connect((self.host, 5556))
        t1=Thread(target=self.threader)
        t1.start()

    def threader(self):
        while True:
            self.changeText()

    def init_window(self):
        self.master.title("User")
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
        self.s.send(str.encode(self.textfield.get('1.0', END)))
        self.textfield.delete('1.0', END)

    def changeText(self):
        '''x=len(text)-3
        txt=text[2:x]
        self.textarea.configure(state='normal')
        self.textarea.insert(END, 'Owner: '+txt+'\n')
        self.textarea.configure(state='disabled')
        def openimg(self):
        subprocess.call('cd\\', shell=False)
        subprocess.call('cd c:\\Users\\computer\\Desktop', shell=False)
        subprocess.call('bh.jpg', shell=False)'''
        text=str(self.s.recv(1024))
        x=len(text)-3
        txt=text[2:x]
        self.textarea.configure(state='normal')
        self.textarea.insert(END,'User: '+ txt+'\n')
        self.textarea.configure(state='disabled')



   

    
root=Tk()
root.geometry("500x600")
app=window(root)
root.mainloop()
