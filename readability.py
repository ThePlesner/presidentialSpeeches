# Importing regular expression-library
import re

# Speeches (.txt) should be named by the year in which they were spoken
# Returns a string containing the whole transcription of the speech


def readSpeech(year):
	# Opens file
	with open(f"./speeches/{year}.txt", "r", encoding="utf-8") as text:
		speech = text.read()
		return speech

# Takes a string and returns the LIX of that string

def calculateLix(speech):
	cleanSpeech = re.sub("\n", " ", speech)
	cleanSpeech = re.sub(r"—|-", " ", cleanSpeech)
	cleanSpeech = re.sub(r"[^a-zA-Z '-]", "", cleanSpeech)

	print(cleanSpeech)
#    numWords =
#    numPeriods =
#    numLongWords =


#! TESTING
calculateLix(readSpeech(2002))
