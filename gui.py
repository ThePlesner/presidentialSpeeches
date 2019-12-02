# 
import tkinter as tk
import webbrowser
import readability
import htmlGenerator
import clouds
import os
from pathlib import Path

def generateOne(year, root):
    clouds.showWordCloud(year)
    window = tk.Toplevel(root)
    
    speech = readability.readSpeech(year)

    lixNumber = readability.calculateLix(speech)
    colemanLiauNumber = readability.calculateColemanLiau(speech)

    listBox = tk.Listbox(window)
    listBox.pack()

    listBox.insert(END, "Indexes for: " + str(year))
    listBox.insert(END, "Lix: " + str(lixNumber))
    listBox.insert(END, "Coleman-Liau: " + str(colemanLiauNumber))


def generateAll():
    htmlGenerator.writeHTML()
    webbrowser.open_new_tab(Path('output/documents', 'overview.html'))


root = tk.Tk()

inputFrame = tk.Frame(root)

inputField = tk.Entry(inputFrame)
inputField.pack(padx=(40, 40), pady=(5, 5))

submitButton = tk.Button(inputFrame, text = "Generate single", command = lambda : generateOne(inputField.get(), root))
submitButton.pack(fill = BOTH, padx=(40, 40), pady=(5, 5))

generateAllButton = tk.Button(inputFrame, text= "Generate all", command = lambda : generateAll())
generateAllButton.pack(fill = BOTH, padx=(40, 40), pady=(5, 5))

infoText = tk.Label(inputFrame, text="This is our (minimalistic) GUI. In the input field you can write a year \n" 
                                  "between 1961 and 2019 and press 'generate single'. This will generate one \n "
                                  "wordcloud for the State of the Union speech for that year, and create a \n"
                                  "new window with the readability indexes. If you press 'generate all' you \n"
                                  "will not need to write a year, as it will generate a html file and open \n"
                                  "it in your default browser. This might take some time but you can follow\n"
                                  "the progress in the console")
infoText.pack()

inputFrame.pack(anchor = CENTER)
root.mainloop()





