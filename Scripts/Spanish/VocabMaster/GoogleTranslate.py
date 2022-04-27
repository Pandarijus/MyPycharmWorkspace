from googletrans import Translator

textNames = ["German.txt","Spanish.txt"]
textName = "German.txt"#"Spanish.txt"

with open("Texts/"+textName) as textFile:
    textLines = textFile.readlines()

languages = ['es','de']
translator = Translator()
for text in textLines:

    outputLanguage = 'de' if textName == "Spanish.txt" else 'es'#take opposite language
    print(translator.detect(text))
    translation = translator.translate(text,outputLanguage)
    print(text[:-1]+" == "+translation.text)





