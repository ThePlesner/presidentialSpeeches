# Imports a class 'WordCloud' from library 'wordcloud' containing necessary methods.
from wordcloud import WordCloud
# Used to check for already existing wordcloud files, as to not generate them every time
import os


def createWordCloud(year):
  with open(f'./speeches/{year}.txt', 'r', encoding='utf-8', errors='replace') as text:
    text = text.read().lower()

    # WordCloud-class generates an object with the height and width props of our wordcloud
    # .generate(text) calls a method (generate_from_frequencies) that uses the object parameters to generate a wordmap.
    # it uses the frequency of each word to adjust font-size of each word and creates a word cloud.
    wordcloud = WordCloud(width=800, height=600).generate(text)
    # to_image then draws an image from the word cloud.
    image = wordcloud.to_image()
    return image


def showWordCloud(year):
  # .show() displays an image using the default application on the computer.
  createWordCloud(year).show()


def saveWordCloud(year):
  filePath = f'./output/images/{year}-wordcloud.png'
  if not os.path.isfile(filePath):
    createWordCloud(year).save(f'./output/images/{year}-wordcloud.png')
