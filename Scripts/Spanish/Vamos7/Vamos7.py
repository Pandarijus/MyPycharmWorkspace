import os
import random
fileSufix = "Ger"
fileName = "Vamos7"#input("Give me the capter name:\n")
files =os.listdir(os.curdir)

for file in files:
    if fileName in file:
        if fileSufix in file:
            germanText = file
        else:
            spanishText = file


def getAllLinesOfText(textName):
    with open(textName,encoding="utf-8") as textFile:
        textLines = textFile.readlines()

    for t in range(len(textLines)):
        textLines[t] = textLines[t][:-1]
    return textLines

germanVocabs = getAllLinesOfText(germanText)
spanishVocabs = getAllLinesOfText(spanishText)

combo = 0
while True:
    rand = random.randrange(len(germanVocabs))
    targetVoc = spanishVocabs[rand]
    voc = germanVocabs[rand]
    inputVoc = input(voc+"\n")#+"   combo: "+str(combo)
    if inputVoc in targetVoc:
        combo +=1
        print("TRUE combo: "+str(combo))
    else:
        combo = 0
        print(voc+" == "+targetVoc)