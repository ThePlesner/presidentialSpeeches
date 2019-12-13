# Imports the WordCloud method to generate wordcloud images
from wordcloud import WordCloud
# Used to generate OS specific file paths and check for existing files
from pathlib import Path
# Used to read a speech
from readability import readSpeech


def createWordCloud(year):
  speech = readSpeech(year)

  # We don't want duplicate words with differing capitalizations in our wordcloud
  speech = speech.lower()

  # First we set size settings with the WordCloud method, 
	# then we generate the wordcloud object
  wordcloud = WordCloud(width=800, height=600).generate(speech)

  # Then we generate an image object from the wordcloud object
  image = wordcloud.to_image()

  return image

def showWordCloud(year):
  # Displays in default image application
  createWordCloud(year).show()


def saveWordCloud(year):
  # Path and name of generated image file
  filePath = Path('output/images', f'{year}-wordcloud.png')

  # Only generates file if it does not exist
  if not filePath.is_file():
    createWordCloud(year).save(filePath)
