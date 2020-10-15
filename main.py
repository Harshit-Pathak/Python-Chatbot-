import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot("Nebula")

convo=[
    'Hello',
    'hi there !',
    'what is your name ?',
    'My name is Nebula , I am created by Harshit',
    'how are you ?',
    'I am doing great these days',
    'It was nice talking to you',
    'thank you',
    'In which city do you live ?',
    'In which language do you speak ?',
    'I mostly talk in english' 
    'I live in Mumbai'
]
trainer = ListTrainer(bot)

#training the bot with trainer

trainer.train(convo)

main = tk.Tk()

main.geometry("500x550")

main.title(" My Chat Bot")
def ask_from_bot():
    query=textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    textF.delete(0,END)

frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#creating text field

textF=Entry(main,font=("Verdana",15))
textF.pack(fill=X,pady=10)

btn=Button(main,text="Ask from bot",font=("Verdana", 15),command=ask_from_bot)
btn.pack()




main.mainloop()
