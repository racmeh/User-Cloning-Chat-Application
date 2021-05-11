from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def train():
    chatbot=ChatBot('Bot')
    trainer=ListTrainer(chatbot)
    fname=open("conversation.txt","r").readlines()
    trainer.train(fname)
    
