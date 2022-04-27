import googletrans

#print(googletrans.LANGUAGES)

t = googletrans.Translator()
ts = t.translate("Hallo",'es','de')
print(ts)