end = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]

y = " y "

start = ["ciento","doscientos","trescientos","cuatocientos","quinietos","seiscientos","setecientos","ochocientos","novecientos"]

numbs = []

file = open("Numbers",encoding="utf-8")
allLines = file.readlines()

for s in start:
    numbs.append(s+"\n")
    for l in allLines:
        numbs.append(s+" "+l)

for n in numbs:
    print(n,end ="")