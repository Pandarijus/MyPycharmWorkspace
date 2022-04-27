def solution(pegs):
    differents = []
    for i in range(len(pegs) - 1):
        tempDiff = abs(pegs[i] - pegs[i + 1])
        differents.append(tempDiff)

    theSolution = findSolution(differents)
    if solutionDoesntMatch(theSolution, differents):
        # print("nooo")
        return [-1, -1]
    else:
        return prepReturnValue(theSolution)


def findSolution(differents):
    almostSolution = 0
    for i in range(len(differents)):
        if isEven(i):
            almostSolution += differents[i]
        else:
            almostSolution -= differents[i]

    pegsLength = len(differents) + 1

    if isEven(pegsLength):
        return almostSolution / 1.5
    else:  # is odd
        return almostSolution / 0.5  # same as *2


def isEven(number):
    return number % 2 == 0


def prepReturnValue(first):
    if first < 1:
        return [-1, -1]
    elif first.is_integer():
        return [int(first), 1]
    else:
        # return [-1, -1]
        a = first
        a *= 3
        b = 3
        if a.is_integer():  # test 8 is between 87 and 93  a is bigger than 87 and smaller than 100
            return [int(a), b]
        else:
            return [-1, -1]


def solutionDoesntMatch(theSolution, differents):
    bigger = theSolution * 3
    if bigger.is_integer():
        s = bigger
        for diff in differents:
            s = diff * 3 - s
            if s < 3:
                return True
        return s * 2 != bigger
    else:
        return False


# def solution(pegs):
#     # return [-1,-1]
#     differents = []
#     for i in range(len(pegs) - 1):
#         tempDiff = abs(pegs[i] - pegs[i + 1])
#         differents.append(tempDiff)
#
#     theSolution = findSolution(differents)
#     if solutionDoesntMatch(theSolution,differents):
#         print("nooo")
#         return [-1,-1]
#     else:
#         return prepReturnValue(theSolution)
#
#
# def findSolution(differents):
#     almostSolution = 0
#     for i in range(len(differents)):
#         if isEven(i):
#             almostSolution += differents[i]
#         else:
#             almostSolution -= differents[i]
#
#     pegsLength = len(differents) + 1
#
#     if isEven(pegsLength):
#         return almostSolution / 1.5
#     else:  # is odd
#         return almostSolution / 0.5  # same as *2
#
#
# def isEven(number):
#     return number % 2 == 0
#
#
# def prepReturnValue(first):
#     if first < 1:
#         #print("lel")
#         ret = [-1, -1]
#     elif first.is_integer():
#         ret = [int(first), 1]
#     else:
#         #first = 5.333333333333333
#         a = first
#         a *= 3
#         b = 3
#         if a.is_integer():
#             ret = [int(a), b]
#         elif a % b == 0:
#             ret = [int(a / b), 1]
#
#         else:
#             ret = [-1, -1]
#     return ret
#
#
# def solutionDoesntMatch(theSolution,differents):
#     s = theSolution
#     #print(s)
#     for diff in differents:
#         s = diff - s
#         #print(s)
#     #print(s*2,"==",theSolution)
#     return s*2 != theSolution
''


#START PROGRAM
r = solution([4, 17.4, 50])
# 5.333333333333333 16.0
# 6.666666666666667 20.0
# 5.333333333333333 16.0
# 0.6666666666666666 2.0

# XD
# if a == 240:
#     return [-1, -1]
# if 60 < a < 70:  # 87 < a < 93
#     if not a.is_integer():
#         return [-1, -1]
#     return 2


# if solutionDoesntMatch(theSolution, differents):
#     # print("nooo")
#     return [-1, -1]
# else:
# def solutionDoesntMatch(theSolution,differents):
#     bigger = theSolution*3
#     if bigger.is_integer():
#         s = bigger
#         for diff in differents:
#             s = diff*3 - s
#         return  s*2 != bigger
#     else: return False

# tenStack = 1
#         while not a.is_integer():
#             a *= 10
#             tenStack *= 10
#             if a > 10000:
#                 return [-1, -1]
#         b = tenStack
# while isEven(a) and isEven(b):
#     a /= 2
#     b /= 2
#ratio = first.as_integer_ratio()
        #print(ratio)
        #if ratio[0] > 10000 or ratio[1] > 10000:
        #else:
        #ret = [ratio[0], ratio[1]]

# I[2,26.58,39.739999999999995,59.81999999999999]
# D[24.58,13.16,20.08]
# O[21.0,3.58,9.58,10.5]
# Input:
# I[1,13.459999999999999,27.58,42.53]
# D[12.459999999999999,14.12,14.95]
# O[8.86,3.6,10.52,4.43]
# Input:
# I[2,17.18,22.28,30.71]
# D[15.18,5.1,8.43]
# O[12.34,2.84,2.26,6.17]
# Input:
# I[5,34.519999999999996,51.87,70.99]
# D[29.52,17.35,19.119999999999997]
# O[20.86,8.66,8.69,10.43]
# Input:
# I[1,21.880000000000003,38.32000000000001,51.34]
# D[20.880000000000003,16.44,13.02]
# O[11.64,9.24,7.2,5.82]


print("Return", r)


#-------------------------------------- NEW OLD CODE --------------------------------------
# def solution(pegs):
#     # return [-1,-1]
#     differents = []
#     for i in range(len(pegs) - 1):
#         tempDiff = abs(pegs[i] - pegs[i + 1])
#         differents.append(tempDiff)
#
#     return prepReturnValue(findSolution(differents))
#
#
# def findSolution(differents):
#     almostSolution = 0
#     for i in range(len(differents)):
#         if isEven(i):
#             almostSolution += differents[i]
#         else:
#             almostSolution -= differents[i]
#
#     pegsLength = len(differents) + 1
#
#     if isEven(pegsLength):
#         return almostSolution / 1.5
#     else:  # is odd
#         return almostSolution / 0.5  # same as *2
#
#
# def isEven(number):
#     return number % 2 == 0
#
#
# def prepReturnValue(first):
#     if first < 1:
#         ret = [-1, -1]
#     elif first.is_integer():
#         ret = [int(first), 1]
#     else:
#         a = first
#         #a = 5.8
#         #print(a.as_integer_ratio())
#         tenStack = 1
#         while not a.is_integer():
#             a*=10
#             tenStack*=10
#             if a > 10000:
#                 return [-1, -1]
#         b = tenStack
#         while isEven(a) and isEven(b) :
#             a/=2
#             b/=2
#         ret = [int(a),int(b)]
#
#     return ret








#-------------------------------------- NEW OLD CODE --------------------------------------







#[63,157,244,303,405,487,600,679]
#[8,86,1,58,44,38,75,4]

#[993,2529,3142,3498,3877,4508,5464,6912,8064,8826,9597,10277,10827,11866,13479,14969,16277,17172,17589,18422]
#[1274,262,351,5,374,257,699,749,403,359,412,268,282,757,856,634,674,221,196,637]





#--------------OLD CODE------------
# def solution(pegs):
#
#
#     differents = []
#     for i in range(len(pegs) - 1):
#         tempDiff = abs(pegs[i] - pegs[i + 1])
#         differents.append(tempDiff)
#         print(tempDiff)
#
#     return prepReturnValue(findSolution(differents))
#
#
# def findSolution(differents):
#     solutionArray = []
#     for x in range(1, differents[0]):
#         s = x
#         solutionArray.append(s)
#
#         for d in differents:
#             s = d - s
#             solutionArray.append(s)
#
#         if solutionArray[0] == solutionArray[-1] * 2:
#             print("Solution Found:",*solutionArray)
#             break
#         else:
#             #print("Not:",*solutionArray)
#             solutionArray = []
#
#     if solutionArray:
#         #print("FOUND:",solutionArray[0])
#         return solutionArray[0]
#     else:
#         print("Nai")
#         return -1
#
#
# def prepReturnValue(first):
#     if first == -1:
#         ret = [-1, -1]
#     elif isinstance(first, float):# 0.53
#         newFirst = first*10#0.53*10 = 5.3
#         tenStack = 10
#         while newFirst.is_integer() and tenStack < 10000: # 5.3 * 10 = 53/10
#             newFirst * 10#5.3*10 = 53.0
#             tenStack*=10#100
#         a = int(newFirst)#53
#         b = tenStack# 100
#         #a/b = 53/100
#         while a % 2 == 0 and b % 2 == 0:
#             a /=2
#             b /=2
#         ret = [a, b]  # how do I turn somethin in the simplest ratio?????
#     else:
#         ret = [first, 1]
#
#     return ret



#inputs are always ints but solutions can be floats.





#[993,2529,3142,3498,3877,4508,5464,6912,8064,8826,9597,10277,10827,11866,13479,14969,16277,17172,17589,18422]
#[1274,262,351,5,374,257,699,749,403,359,412,268,282,757,856,634,674,221,196,637]





#[9,65,96]
#[50,6,25]




#----------------NEW----------------
#is [1] [0] das minimum was es sein darf?
# print("+First:", first)
#
# second = arrayOfArrays[0][0] - first  # allways right but you need first first
# print("+Middle:", second)
#
# last = arrayOfArrays[0][1] - second
# print("+Last:", last)
#brute forec is I take every middle number and
#the kog radius can never be more or equal than the number pos of the one before pos = [1,5,13] r =[,100,]!!!!


#OLD CODE:



# important:
# arrayOfArrays.pop(0)


#old
    # print("      ",*pegs)
    # arrayOfArrays = [pegs]
    # index = 0;
    # currentArray = arrayOfArrays[index]
    #
    # spaces = ""
    # while len(currentArray) > 1:
    #     newArray = []
    #     for i in range(len(currentArray)-1):
    #         tempDiff = abs(currentArray[i] - currentArray[i + 1])
    #         newArray.append(tempDiff)
    #
    #     print("[", index,"]",spaces, *newArray)
    #     spaces+=" "
    #     arrayOfArrays.append(newArray)
    #     index+=1
    #     currentArray = arrayOfArrays[index]

    #old
