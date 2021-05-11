from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import pickle
#import mysql.connector

def processText(string):
    word_tokens=process(string)
    request=""
    for s in word_tokens:
        temp=preprocess(s)
        request+=temp+" "
    print(request)
        
    #store(request)
    #insertdb(tagged)

def processResponse(string):
    word_tokens=process(string)
    request=""
    for s in word_tokens:
        temp=preprocess(s)
        request+=temp+" "
    print(request)
    #store(request)
    #insertdb(tagged)

def store(string):
    file=open("conversation.txt", "a")
    file.write(string+"\n")
    file.close()
    
'''
def insertdb(tagged):
    conn=mysql.connector.connect(  host="localhost", user="root", passwd="", database='chatbot')
    c=conn.cursor()
    nn=""
    prp=""
    vbp=""
    rb=""
    #c.execute("CREATE DATABASE chatbot")
    #c.execute("CREATE TABLE user (NN VARCHAR(255), PRP VARCHAR(255), VBP VARCHAR(255), RB VARCHAR(255))")
    for i in tagged:
        if i[1]=="NN":
            nn=nn+i[0]
        elif i[1]=="VBP":
            vbp=vbp+i[0]
        elif i[1]=="PRP":
            prp=prp+i[0]
        elif i[1]=="rb":
            rb=rb+i[0]
    query='\''+nn+'\' , '+'\''+prp+'\' , '+'\''+vbp+'\' , '+'\''+rb+'\''
    c.execute("INSERT INTO user values("+query+")")
    c.close()
'''
def process(string):
    string1=sent_tokenize(string)
    string2=word_tokenize(string)
    '''
    stop_words=set(stopwords.words('english'))
    filtered_sentence=[]
    s=[]
    #lemmatizer=WordNetLemmatizer()
    ps=PorterStemmer()
    for w in string2:
        if w not in stop_words:
            filtered_sentence.append(w)
    for w in filtered_sentence:
        #s=s.append(lemmatizer.lemmatize(w))
        s.append(ps.stem(w)
    return nltk.pos_tag(s)'''
    return string2
  

def preprocess(string):
    s=""
    fname="supporting program\\"+string[0]
    fname=fname+"abbr.pickle"
    try:
        file=open(fname, "rb")
        dict={}
        dict=pickle.load(file)
        file.close()
        if string in dict:
            string=dict[string]
    except Exception as e:
        print(e)
    return string

processText("Hi. How are you")
processResponse("I m A3")
