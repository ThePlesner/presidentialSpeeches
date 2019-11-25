from tkinter import *
import clouds



def generateWordCloud(year):
    clouds.showWordCloud(year)

    

root = Tk()
root.geometry("500x500")

inputFrame = Frame(root)

submitButton = Button(inputFrame, text = "submit", command = generateWordCloud(inputField.get()))
submitButton.pack(fill = X, side = RIGHT)

inputField = Entry(inputFrame)
inputField.pack()

inputFrame.pack(anchor = CENTER)
root.mainloop()



#root = Tk()
#w = Label(root, text="Hello")
#w.pack()
#
#root.mainloop()




