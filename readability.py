import re  # Importing regular expression-library
from pathlib import Path  # Used to generate OS specific file paths

# Speeches (.txt) are named by the year in which they were spoken
# Returns a string containing the whole transcription of the speech
def readSpeech(year):
  filePath = Path('speeches', f'{year}.txt')

  # errors='replace' is used to work around decoding errors, since it would unnecessarily time consuming to make sure all the speeches are in utf-8
  with open(filePath, 'r', encoding='utf-8', errors='replace') as textFile:
    speech = textFile.read()
    return speech

# Takes a text string and removes newlines, dashes, and some symbols
def initialCleaning(speech):
  # Substitutes first argument with the second argument
  cleanSpeech = re.sub(r"\n", " ", speech)
  cleanSpeech = re.sub(r"—|-", " ", cleanSpeech)
  cleanSpeech = re.sub(r"[^a-zA-Z \.'\?!]", "", cleanSpeech)
  return cleanSpeech

# LIX = (number of words / number of sentences) + (number of long words * 100) / number of words
def calculateLix(speech):
  cleanSpeech = initialCleaning(speech)

  # Splitting on space gives us a list of just the words
  numWords = len(cleanSpeech.split())

  # Every period, question mark and exclamation point indicates the end of a sentence
  numSentences = cleanSpeech.count('.') + cleanSpeech.count('?') + cleanSpeech.count('!')

  # We now remove periods and quotation marks
  cleanSpeech = re.sub(r"\.|\?|!", "", cleanSpeech)

  # We make another list of only words
  words = cleanSpeech.split()

  # And count every word with more than 6 characters
  numLongWords = 0
  for word in words:
    if len(word) > 6:
      numLongWords += 1

  lix = (numWords / numSentences) + ((numLongWords * 100) / numWords)
  return round(lix, 2)

# CLI = 0.0588 * (avg num of letters / 100 words) - 0.296 * (avg num of sentences / 100 words) - 15.8
def calculateColemanLiau(speech):
  cleanSpeech = initialCleaning(speech)

  # Every period, question mark and exclamation point indicates the end of a sentence
  numSentences = cleanSpeech.count('.') + cleanSpeech.count('?') + cleanSpeech.count('!')

  # Splitting on space gives us a list of just the words
  numWords = len(cleanSpeech.split())
  sentencesPer100Words = numSentences / numWords * 100

  # Finds all letters in the text
  numWordChars = len(re.findall(r'\w', cleanSpeech))
  lettersPer100Words = numWordChars / numWords * 100

  cli = 0.0588 * lettersPer100Words - 0.296 * sentencesPer100Words - 15.8
  return round(cli, 2)

# Returns a tuple with [0] == CLI and [1] == LIX
def readability(year):
  speech = readSpeech(year)
  return (calculateColemanLiau(speech), calculateLix(speech))
