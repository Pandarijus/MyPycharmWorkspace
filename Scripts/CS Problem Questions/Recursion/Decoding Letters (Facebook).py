#every letter is number 1 -> 26. I need to build numbers. Feels like rekursion like the fibenacci sequence
a = []
def solution(inputNumber):

    for x in range(len(inputNumber)):
        do(inputNumber[x])
        if x+1 < len(inputNumber):
            do(inputNumber[x] + inputNumber[x+1])

def do(string):
    if checkIfValid(string):
        a.append(encode(string))

def checkIfValid(string):
    i = int(string)
    return 0 < i < 27

def encode(string):
    i = int(string)
    si = chr(i + ord('a')-1)
    #print(i,"->",si)
    return si

solution("133")#13 -> [ac,m]. 133 -> [mc,acc]. 123 -> [abc,aw,lc]. 01 -> None. 10 -> j
print(*a)