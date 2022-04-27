import random

def generateExamples(maxLenght = 3):
    maxNumber = 10
    generatedSolution = []
    calculatedDiff = []
    generatedInput = []
    lengthOfSolution = maxLenght
    for x in range(lengthOfSolution):#create solution array
        #generatedSolution.append(round( random.uniform(1, maxNumber + 1),2))
        generatedSolution.append(random.randrange(1, maxNumber + 1)/1.5)
        #generatedSolution.append(random.randrange(1, maxNumber + 1))
    generatedSolution[0] = generatedSolution[-1] * 2

    for x in range(lengthOfSolution - 1):
        st = generatedSolution[x] + generatedSolution[x + 1]
        calculatedDiff.append(st)

    out = random.randrange(1, maxNumber + 1)
    generatedInput.append(out)

    for st in calculatedDiff:
        out += st
        generatedInput.append(out)


    print("Input:")
    print(getArrayToString(generatedInput,"I"))
    print(getArrayToString(calculatedDiff,"D"))
    print(getArrayToString(generatedSolution,"O"))



def getArrayToString(array,prefix = ""):
    aStr = prefix+"["
    for a in array:
        aStr += str(a) + ","
    aStr = aStr[:-1]
    aStr += "]"
    return aStr


#test = 0.25
#t = test.as_integer_ratio()
#print(t[0],t[1])
#print()
for x in range(1):
    #r = random.randrange(1, 10 + 1) / 1.5
    print((12.0).is_integer())
    #print(1.233/ 1.5)
    #generateExamples(4)

