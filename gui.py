from tkinter import *
from readability import *
import clouds



def generateWordCloud(year):
    clouds.showWordCloud(year)

def showLix(year):
    speech = readSpeech(year)

root = Tk()
root.geometry("500x500")

inputFrame = Frame(root)

inputField = Entry(inputFrame)
inputField.pack(side=LEFT)

submitButton = Button(inputFrame, text = "wordcloud", command = lambda : generateWordCloud(inputField.get()))
submitButton.pack(side=LEFT)

lixButton = Button(inputFrame, text = "lix", )

inputFrame.pack(anchor = CENTER)
root.mainloop()



#root = Tk()
#w = Label(root, text="Hello")
#w.pack()
#
#root.mainloop()




