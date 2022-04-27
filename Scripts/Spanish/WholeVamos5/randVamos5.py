import os
import random

def getAllLinesOfText(textName):
    with open(textName,encoding="utf-8") as textFile:
        textLines = textFile.readlines()

    for t in range(len(textLines)):
        textLines[t] = textLines[t].replace('\n','')
    return textLines

germanVocabs = getAllLinesOfText("German")
spanishVocabs = getAllLinesOfText("Spanish")

vocsDoneToday = 0
combo = 0
notTrue = True
while True:
    notTrue = not notTrue
    rand = random.randrange(len(germanVocabs))
    targetVoc = germanVocabs[rand] if notTrue else spanishVocabs[rand]
    voc = spanishVocabs[rand] if notTrue else germanVocabs[rand]
    while True:#loop untill you get the vocab right
        inputVoc = input(voc+"\n"+":")
        if inputVoc.lower() in targetVoc.lower():
            combo +=1
            vocsDoneToday+=1
            print("TRUE combo: "+str(combo))
            if vocsDoneToday == 10:
                print("You are done for today")
            break#stop looping the same vocab
        else:
            combo = 0
            print(inputVoc+" != ["+voc+"] == ["+targetVoc+"]")

