import re


def readSpeech(year):
    # Opens file 
    text = open(f"./speeches/{year}.txt", "r", encoding="utf-8")
    speech = text.read()
    text.close()
    return speech
    

def calculateLix(speech):
    cleanSpeech = re.sub("\n", " ", speech)
    cleanSpeech = re.sub(r"—|-", " ", cleanSpeech)
    cleanSpeech = re.sub(r"[^a-zA-Z '-]", "", cleanSpeech)
    
    
    
    print(cleanSpeech)
#    numWords = 
#    numPeriods =
#    numLongWords =

calculateLix(readSpeech(2002))