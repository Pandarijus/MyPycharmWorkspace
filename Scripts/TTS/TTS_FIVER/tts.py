from gtts import gTTS as g

path = "150Cashtxt.txt"

text = open(path,encoding="utf-8").read()
#print(text)
mp3Name = path[:-4]+".mp3"
g(text,lang='de').save(mp3Name)

