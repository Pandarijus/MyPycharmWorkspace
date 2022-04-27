from VocabClass import VocabClass

fileName = "Vamos7"
fileSufix = "Ger"

germanVocabs,spanishVocabs = VocabClass.getBothTexts(fileName,fileSufix)

combo = 0
while True:
    targetVoc, voc = VocabClass.getRandomVocab(germanVocabs,spanishVocabs)
    inputVoc = input(voc+"\n")
    if inputVoc in targetVoc:
        combo +=1
        print("TRUE combo: "+str(combo))
    else:
        combo = 0
        print(voc+" == "+targetVoc)