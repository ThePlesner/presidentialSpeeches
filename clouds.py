# Imports the WordCloud method to generate wordcloud images
from wordcloud import WordCloud
# Used to generate OS specific file paths and check for existing files
from pathlib import Path


def createWordCloud(year):
  filePath = Path('speeches', f'{year}.txt')
  
  # errors='replace' is used to work around decoding errors, since it would unnecessarily time consuming to make sure all the speeches are in utf-8
  with open(filePath, 'r', encoding='utf-8', errors='replace') as textFile:
    # We don't want duplicate words with differing capitalizations
    speech = textFile.read().lower()

    # First we set size settings with the WordCloud method, then we generate the wordcloud object
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
  # if not os.path.isfile(filePath):
  if not filePath.is_file():
    createWordCloud(year).save(filePath)
