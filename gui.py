import tkinter as tk # Used to generate native graphical user interfaces
import webbrowser # Used to open our overview in the default browser
import readability # Our own functions to generate readability numbers
import htmlGenerator # Our own functions to generating an html file with an overview of our data
import clouds # Our own functions to generate word clouds
from pathlib import Path # Used to generate OS specific file paths

# Shows a wordcloud and readability indices for one year
def generateOne(year, root):
  # Creates and shows the wordcloud for the selected year
  clouds.showWordCloud(year)

  # Toplevel() creates a new "widget" as a new window
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

# Creates two buttons; one for generating a single speech, one for generating all speeches
# The command argument is the callback function to run when the button is clicked. The anonymous lambda function calls
# generateOne() with our arguments, as to not call this function immediately when the button is created
generateOneButton = tk.Button(inputFrame, text="Show For Year", command=lambda: generateOne(inputField.get(), root))
# Sets padding and width (fill) of button
generateOneButton.pack(fill=tk.BOTH, padx=(40, 40), pady=(5, 5))

generateAllButton = tk.Button(inputFrame, text="Generate all", command=generateAll)
# Sets padding and width (fill) of button
generateAllButton.pack(fill=tk.BOTH, padx=(40, 40), pady=(5, 5))

# Adds a small guide to the window
infoText = tk.Label(inputFrame, text="This is our (minimalistic) GUI. In the input field you can write a year\n"
                                     "between 1961 and 2019 and press 'Show For Year'. This will generate one\n "
                                     "wordcloud for the State of the Union speech for that year, and create a\n"
                                     "new window with the readability indices. If you press 'Generate All' you\n"
                                     "will not need to write a year, as it will generate an HTML file,\n"
                                     "wordcloud images, and open it in your default browser.\n"
                                     "This might take some time.")
infoText.pack()

# Packs the frame and attaches it to the middle of the window
inputFrame.pack(anchor=tk.CENTER)

# Runs the GUI
root.mainloop()