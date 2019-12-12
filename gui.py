import tkinter as tk  # Used to generate native graphical user interfaces
import webbrowser  # Used to open our overview in the default browser
import readability  # Our own functions to generate readability numbers
import htmlGenerator # Our own functions to generating an html file with an overview of our data
import clouds  # Our own functions to generate word clouds
import json #Imports json for parsing json files
from pathlib import Path  # Used to generate OS specific file paths

def getPresident(year):
  currentPresident = ""
  
  # Opens and reads json file
  presidentialPeriods = open('presidentialPeriods.json', 'r', encoding='utf-8').read()

  # Parses json into python
  presidentialPeriods = json.loads(presidentialPeriods)

  for president in presidentialPeriods:
    #if year in range(president['period_from'], president['period_to'] + 1):
      #currentPresident = president['name']
      print(president["period_from"])
  
  return currentPresident



# Shows a wordcloud and readability indices for one year
def generateOne(year, root):
  # Creates and shows the wordcloud for the selected year
  clouds.showWordCloud(year)

  # Creates a new "widget" as a new window
  window = tk.Toplevel(root)

  # Get the two indices as a tuple from our own library
  readabilityNums = readability.readability(year)
  CLI = readabilityNums[0]
  LIX = readabilityNums[1]

  # A listbox is created as it allowed us to display information in a list format
  listBox = tk.Listbox(window)
  # pack() organizes the elements before attaching it to the parent element (window)
  listBox.pack()

  # Inserts as list elements the year and indices
  listBox.insert(tk.END, f"Indexes for: {year}")
  listBox.insert(tk.END, f"{getPresident(year)}")
  listBox.insert(tk.END, f"LIX: {LIX}")
  listBox.insert(tk.END, f"CLI: {CLI}")

# Generates and shows wordclouds and readability indices for all existing speeches
def generateAll():
  # Writes the html file
  htmlGenerator.writeHTML()

  # Opens the file in the default browser
  webbrowser.open_new_tab(Path('output/documents', 'overview.html'))


# Creates the root window
root = tk.Tk()

# Creates a frame widget
inputFrame = tk.Frame(root)

# Creates an input field and adds that to the frame widget
inputField = tk.Entry(inputFrame)
# Sets the padding of the input field
inputField.pack(padx=(40, 40), pady=(5, 5))

'''Creates two buttons; one for generating a single speech, one for generating all speeches
   The command argument is the callback function to run when the button is clicked. The anonymous lambda function calls
   generateOne() with our arguments, as to not call this function immediately when the button is created '''
generateOneButton = tk.Button(inputFrame, text="Show For Year", command=lambda: generateOne(inputField.get(), root))
# Sets padding and width (fill) of button
generateOneButton.pack(fill=tk.BOTH, padx=(40, 40), pady=(5, 5))

generateAllButton = tk.Button(inputFrame, text="Generate All", command=generateAll)
# Sets padding and width (fill) of button
generateAllButton.pack(fill=tk.BOTH, padx=(40, 40), pady=(5, 5))

# Adds a small guide to the window
infoText = tk.Label(inputFrame, text= "To see a 'topical' wordcloud for a given year:\n"
                                      "Write a year between 1961 and 2019 in the input field\n"
                                      "and click 'Show For Year'\n"
                                      "\n"
                                      "To see an overview of all available speeches' data:\n"
                                      "Click 'Generate All'.\n"
                                      "This might take a while.")
infoText.pack()

# Packs the frame and attaches it to the middle of the window
inputFrame.pack(anchor=tk.CENTER)

# Runs the GUI
root.mainloop()
