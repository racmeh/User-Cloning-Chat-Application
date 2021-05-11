import naturalLangProc as nlp
import pickle

def nlpmodule(string):
    obj=string.split("\n")
    print(obj)
    for s in obj:
       print(s) 
       st=s.split(":", 2)
       print(st[0])
       if st[0]=="User" :
           nlp.processText(st[1])
       elif st[0]=="You":
           nlp.processResponse(st[1])
    

   
