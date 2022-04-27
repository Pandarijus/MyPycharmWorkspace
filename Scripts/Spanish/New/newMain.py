import random

fileName = "Vamos5"#input("Give me the capter name:\n")
lines = open("voc2",encoding="utf-8").readlines()



combo = 0
while True:
    rand = random.randrange(len(lines))
    #print(rand)
    lin = str(lines[rand])
    #print(lin)
    l = lin.split(":")
    targetVoc = l[0] if combo % 2 == 0 else l[1]
    voc = l[1] if combo % 2 == 0 else l[0]
    inputVoc = input(voc+":")#+"   combo: "+str(combo)
    if inputVoc.lower() in targetVoc.lower():
        combo +=1
        print("TRUE combo: "+str(combo))
    else:
        combo = 0
        print(voc+" == "+targetVoc)