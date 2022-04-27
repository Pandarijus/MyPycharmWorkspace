from gtts import gTTS as g

wantToReadFromFile = input("Wollen Sie : \n Text Aus Einer Datei Lesen [0]\n oder Text Einfügen [1]\n") == "0"

language = 'de' if input("Bestimme eine Sprache: \n Druecke [0] fuer Deutsch und [1] fuer Englisch \n")== "0"else 'en'

if not wantToReadFromFile:
    mp3Name = input("Schreibe mir einen Namen die diese mp3 Datei bekommen soll:\n")+".mp3"
    path = mp3Name
    txt = input("Schreibe mir den Text den ich dir sprechen soll: \n")
else:
    pathTextfile = input("Schreibe mir einen Namen die diese mp3 Datei bekommen soll:\n")
    if ".txt" not in pathTextfile:
        pathTextfile = pathTextfile+".txt"
    txt = open("t.txt", encoding='utf-8').readlines()
    path = pathTextfile[:-3]+"mp3"
    input(path)

text = ''.join(filter(str.isalnum, txt))#removes special caracters.  MAYBE REMOVE NUMBERS ALSO

g(text,lang=language).save(path)
#   input(path)
