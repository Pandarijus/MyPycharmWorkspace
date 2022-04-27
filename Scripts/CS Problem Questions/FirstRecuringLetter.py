def solution(inputString):
    for x in range(0,len(inputString)-1):
        tempChar = inputString[x]
        for y in range(x+1, len(inputString)):
            if tempChar == inputString[y]:
                return tempChar
    #for ends here
    return None


def solution2(inputString):
    letters = []
    for letter in inputString:
        if letter in letters:
            return letter
        else:
            letters.append(letter)
    # for ends here
    return None

def solution3(inputString):
    letters = {}
    for letter in inputString:
        if letter in letters:
            return letter
        else:
            letters[letter] = 1
    # for ends here
    return None

s = solution3("JVBDBDSNSNSABAANANANANAN")
print(s)