# For generating HTML
import dominate
# For easy access to HTML tag methods
from dominate.tags import *
# Our own functions to generate readability numbers
import readability
# Our own functions to generate word clouds
import clouds
# For parsing the json with presidential periods data
import json

# Counter variable for the progress bar in the interface
progress = 0

# Opens and reads json file
presidentialPeriods = open('presidentialPeriods.json', 'r', encoding='utf-8').read()
# Parses json into python
presidentialPeriods = json.loads(presidentialPeriods)


def writeHTML():
  # Generates an empty html-template with only a title
  document = dominate.document(title="Presidential Speeches")
  # Links to the style document
  with document.head:
    link(rel='stylesheet', href='styles.css')

  # Generates a list of presidents
  presidencies = ul()
  for president in presidentialPeriods:
    # Adds a row (list item) for each president's name in the json data
    presidentContainer = li(h1(president['name']))

    # Adds cell data for each year of the presidency (taken from json data)
    for year in range(president['period_from'], president['period_to'] + 1):
      # Handles missing speech files
      try:
        # Adds a box with every speech's data
        presidentContainer.add(generateSpeechBox(year))
        # Every speech adds 1 to the progress
        progress += 1
      except:
        print(f"The speech from {year} does not exist.")

    # The unordered list can be manipulated like a python list:
    presidencies += presidentContainer

  # Appends the whole list to the HTML document's body
  document.body.add(presidencies)

  filePath = Path('output/documents', 'overview.html')
  # Writes the document to an html-file
  with open(filePath, 'w', encoding='utf-8') as file:
    # the DOM object needs to be converted to a string to do so
    file.write(str(document))

def generateSpeechBox(year):
  # Calculating readability numbers from imported file
  readabilityNums = readability.readability(year)
  CLI = readabilityNums[0]
  LIX = readabilityNums[1]

  # Generating a word cloud image, if it does not already exist for the given year
  clouds.saveWordCloud(year)

  # Generates a div for every year's speech
  speechBox = div(className="speech-box")
  # Generating a heading with the given year
  yearHeading = h2(year)
  # Generating a div with headings for the readability numbers
  readabilityBox = div(h3(f"Coleman-Liau Index: {CLI}"), h3(f"LIX: {LIX}"))
  readabilityBox['class'] = 'readability-box'
  # Generating a div for text elements for easier layout
  textBox = div(className="text-box")
  # Putting the text elements together for layouting
  textBox.add(yearHeading, readabilityBox)
  # Adds the wordcloud image and textBox to the speechBox
  speechBox.add(img(src=f"../images/{year}-wordcloud.png")) # Browser does the path OS-conversion for us this time
  speechBox.add(textBox)
  
  return speechBox

