import os
import random

class VocabClass:
    @staticmethod
    def getBothTexts(baseName, sufix, inOtherDir=None):
        if inOtherDir:
            files = os.listdir(inOtherDir)
        else:
            files = os.listdir(os.curdir)

        for file in files:
            if baseName in file:
                if sufix in file:
                    germanVocabs = VocabClass.getAllLinesOfText(file)
                else:
                    spanishVocabs = VocabClass.getAllLinesOfText(file)
        return germanVocabs,spanishVocabs

    @staticmethod
    def getAllLinesOfText(textName):
        with open(textName, encoding="utf-8") as textFile:
            textLines = textFile.readlines()

        for t in range(len(textLines)):
            textLines[t] = textLines[t][:-1]
        return textLines

    @staticmethod
    def getRandomVocab(germanVocabs,spanishVocabs):
        rand = random.randrange(len(germanVocabs))
        targetVoc = spanishVocabs[rand]
        voc = germanVocabs[rand]
        return  targetVoc,voc


