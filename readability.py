# Importing regular expression-library
import re

# Speeches (.txt) should be named by the year in which they were spoken
# Returns a string containing the whole transcription of the speech


def readSpeech(year):
  # Opens file
  with open(f"./speeches/{year}.txt", "r", encoding="utf-8") as text:
    speech = text.read()
    return speech


def initialCleaning(speech):
  cleanSpeech = re.sub(r"\n", " ", speech)
  cleanSpeech = re.sub(r"—|-", " ", cleanSpeech)
  cleanSpeech = re.sub(r"[^a-zA-Z \.'\?!]", "", cleanSpeech)
  return cleanSpeech

# Takes a string and returns the LIX of that string


def calculateLix(speech):
  cleanSpeech = initialCleaning(speech)

  numWords = len(cleanSpeech.split())
  numPeriods = cleanSpeech.count(
      '.') + cleanSpeech.count('?') + cleanSpeech.count('!')

  # We now remove periods and quotation marks
  cleanSpeech = re.sub(r"\.|\?|!", "", cleanSpeech)
  words = cleanSpeech.split()
  numLongWords = 0
  for word in words:
    if len(word) > 6:
      numLongWords += 1

  lix = (numWords/numPeriods) + ((numLongWords * 100) / numWords)
  return round(lix, 2)  # 2 digits


def calculateColemanLiau(speech):
  cleanSpeech = initialCleaning(speech)

  numSentences = cleanSpeech.count(
      '.') + cleanSpeech.count('?') + cleanSpeech.count('!')
  numWords = len(cleanSpeech.split())
  sentencesPer100Words = numSentences/numWords * 100

  numWordChars = len(re.findall(r'\w', cleanSpeech))
  lettersPer100Words = numWordChars/numWords * 100

  cli = 0.0588*lettersPer100Words - 0.296*sentencesPer100Words - 15.8
  # return round(cli, 2)
  return cli


def calculateDaleChall(speech):
  cleanSpeech = initialCleaning(speech)

# Returns a tuple with [0] == CLI and [1] == LIX


def readability(year):
  speech = readSpeech(year)
  return (calculateColemanLiau(speech), calculateLix(speech))


# TEST
#print(readability(2002)[0], readability(2002)[1])
print(readability(2002))
