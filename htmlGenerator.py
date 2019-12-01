# For generating HTML
import dominate
from dominate.tags import *
# Our functions to generate readability numbers
import readability
# Our functions to generate word clouds
import clouds
# For parsing the json with presidential periods
import json

# Parses json into python
presidentialPeriods = open('presidentialPeriods.json', 'r', encoding='utf-8')
presidentialPeriods = json.loads(presidentialPeriods.read())


def writeHTML():
  # Generates an html-template
  document = dominate.document(title="Presidential Speeches")
  # Links to the style document
  with document.head:
    link(rel='stylesheet', href='styles.css')

  # Generates a list of presidents
  presidencies = ul()
  for president in presidentialPeriods:
    # Adds a row for each president
    presidentContainer = li(h1(president['name']))

    # Adds cell data for each year of the presidency
    for year in range(president['period_from'], president['period_to'] + 1):
      # Handles missing speeches
      try:
        presidentContainer.add(generateDiv(year))
        print(str(year) + " done")
      except:
        print(f"The speech from {year} does not exist.")

    presidencies += presidentContainer

  document.body.add(presidencies)

  # Writes the document to an html-file
  with open('./output/documents/overview.html', 'w', encoding='utf-8') as file:
    file.write(str(document))

def generateDiv(year):
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
  speechBox.add(img(src=f"../images/{year}-wordcloud.png"))
  speechBox.add(textBox)
  
  return speechBox

