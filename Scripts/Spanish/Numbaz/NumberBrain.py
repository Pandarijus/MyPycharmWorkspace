from Bigbrain import *

index = 0#int(input("Index of game = Numbers:[0]   Dias:[1]  "))
games = ["Numbers2","Dias"]

file = open(games[index],encoding="utf-8")

allLines = file.readlines()


def getRandom(specificNumber = None):
    if specificNumber is None:
      return  np.random.randint(0, len(allLines))
    else:
        wantedNumber = str(specificNumber)
        count = 0
        maxSearch = 1000
        rand = np.random.randint(0, len(allLines))
        while not wantedNumber in str(rand):
            rand = np.random.randint(0, len(allLines))
            if count >= maxSearch:
                break
        return rand

if checkIfSringsAreEqual(games[index],"Numbers2"):

    while True:

        rdm = getRandom()# uncomment if you want to get random numbers
        #rdm = int(input("Number:"))-1
        rdmDisplay = str(rdm+1);

        inp = input(f"[{rdmDisplay}] == ")
        if inp in allLines[rdm]:
            print("YEP")
        else:
            print(f"|{rdmDisplay}|"+ " == " + str(allLines[rdm]))

elif checkIfSringsAreEqual(games[index],"Dias"):
    while True:
        rdm = np.random.randint(0, len(allLines))
        rdmLine = allLines[rdm].split('=')

        inp = input(f"[{rdmLine[0]}] == ")
        if inp in allLines[rdm]:
            print("YEP")
        else:
            print(rdmLine[0]+ " == " +rdmLine[1])






