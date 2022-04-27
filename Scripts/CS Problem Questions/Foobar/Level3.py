def solution(n):
    maxStairLenght = getWhatTheMaxWidthOfAStairIs(n)
    dic = getDic(maxStairLenght)
    everyStartArray = getEveryStartArray(n,maxStairLenght,dic)

    return getSolution(everyStartArray)

def getSolution(everyStartArray):
    output = []

    for startArray in everyStartArray:
        line = generateArray(startArray)
        output.extend(line)
    return output#"!WORK IN PROGRESS!"


def generateArray(startArray):
    output = []
    #even = True
    isNotTwo =  len(startArray) != 2
    if isNotTwo:
        indexToChange = 2
        changingNumber = startArray[indexToChange]  # this is always the index that changes first
    while checkIfArrayIsDESC(startArray):
        output.append(startArray.copy())
        startArray[0] -= 1
        startArray[1] += 1
        if isNotTwo:
            if not checkIfArrayIsDESC(startArray):
                changingNumber += 1
                startArray = calcListFromOneNumberNew(changingNumber, startArray, indexToChange)

            if not checkIfArrayIsDESC(startArray):
                # I CHANGE THE INDEX HERE BUT I ONLY DO IT TO RIGHT BUT I NEED IT TO GO LEFT TOO.

                #--------------------------------------------------------------------

                indexToChange += 1# somehow go back if everthing was explored and make the pev index one higher
                # how do I know if everything was explored?

                    #even = not even
            # if even:
            #     # print("ChangedIndexToRight")
            #     else:
            #         #print("ChangedIndexToLeft")
            #         startArray[0] += 2
            #         startArray[indexToChange] -= 1
            #         indexToChange -= 1
            #         startArray[indexToChange] -= 1
            #         even = not even
            #         #print("!!!!!!!!",startArray[indexToChange])

                # --------------------------------------------------------------------

                if len(startArray) > indexToChange:
                    #print("Hi")
                    changingNumber = startArray[indexToChange]
                    changingNumber += 1
                    startArray = calcListFromOneNumberNew(changingNumber, startArray, indexToChange)
                else:

                    #print("END")
                    break#all is done




    return output






def calcListFromOneNumberNew(changingNumber,startArray,indexToChange):

    subArray = startArray[indexToChange +1:]
    n = sum(startArray)
    lenght =len(startArray)
    #print(n)
    #print(subArray)
    #print("I:",indexToChange)
    #print("L:",lenght)

    subArray.reverse()
    array = []
    array.extend(subArray)
    array.append(changingNumber)



    startRange = len(subArray)
    endRange = lenght -2

    #print("from:", startRange, "To:", endRange)
    for l in range(startRange,endRange):
        array.append(array[l] + 1)
    theSum = sum(array)
    biggest = n - theSum
    array.append(biggest)
    array.reverse()
    #print("Generated List:",array)
    return array



# def calcMaxOfLastNumber(array): #probs useless
#     l =  len(array)-1
#     n = sum(array)
#
#     theMax = getWhatTheMaxWidthOfAStairIs(n)-l
#     return theMax

def checkIfArrayIsDESC(array):

    for i in range(len(array)-1):
        if array[i]<=array[i+1]:# if left is smaller than right :[1,5]
            #print(array,"NO")
            return False
    #print(array,"Yes")
    return True

    #--------------------------------------------- Continue Here -------------------------------------




def getEveryStartArray(n,maxStairLenght,dic):
    everyStartArray = []
    for m in range(2,maxStairLenght+1):
        startArray = getStartArray(n, m, dic)
        everyStartArray.append(startArray)
    return everyStartArray

def getStartArray(n, l, dic):
    l -=1
    su = sum(list(dic[l]))
    startNumber = n- su
    startArray = [startNumber]
    startArray.extend(dic[l])
    #print("StartArray:",startArray)
    return startArray


def getWhatTheMaxWidthOfAStairIs(n):
    add = 0
    for i in range(1,201):
        add += i
        if add > n:
            index = i-1#prev index
            return index



def getDic(l):
    dic = {}
    for a in range(1,l+1):
        key,array = getAddorialArray(a)
        array.reverse()
        dic[key] = array
    #print(dic)
    return dic


def getAddorialArray(m):
    add = 0
    steps = []
    for i in range(1, m + 1):
        add += i
        steps.append(i)
    return i,steps #make key 1 bigger so it makes more sence

for i in range(30,31):
    s = solution(i)
    print("(",i,")","Lenght:", len(s))
    print(s)

# #startArray = [11,2, 1]
# output = []
# third = startArray[2]
# while startArray[2] < startArray[1] < startArray[0]:
#     while startArray[1] < startArray[0]:
#         output.append(startArray.copy())
#         startArray[0] -= 1
#         startArray[1] += 1
#     third+=1
#     startArray = calcListFromOneNumber(third,sum(startArray),len(startArray))
# #print(output)
# return output






# def calcListFromOneNumber(third, n, lenght):#calcListFromOneNumber(changingNumber, sum(startArray), len(startArray))
#     array = [third]
#     for l in range(lenght - 2):
#         array.append(array[l] + 1)
#     theSum = sum(array)
#     biggest = n - theSum
#     array.append(biggest)
#     array.reverse()
#     # print("Generated List:",array)
#     return array




# def startArrayWithLengthOf2(startArray):
#     #startArray = [13, 1]
#     output = []
#     while arrayIsDESC(startArray):
#         output.append(startArray.copy())
#         startArray[0] -= 1
#         startArray[1] += 1
#     return output


# def startArrayWithLengthOf3(startArray):
#     output = []
#     indexToChange = 2
#     changingNumber = startArray[indexToChange]  # this is always the index that changes first
#     while arrayIsDESC(startArray):
#         output.append(startArray.copy())
#         startArray[0] -= 1
#         startArray[1] += 1
#         if not arrayIsDESC(startArray):
#             changingNumber += 1
#             startArray = calcListFromOneNumberNew(changingNumber, startArray, indexToChange)
#     return output
#
#
#
#
#
#
# def startArrayWithLengthOf4(startArray):
#     output = []
#     indexToChange = 2
#
#     changingNumber = startArray[indexToChange]  # this is always the index that changes first
#     while arrayIsDESC(startArray):
#         output.append(startArray.copy())
#         startArray[0] -= 1
#         startArray[1] += 1
#         if not arrayIsDESC(startArray):
#             changingNumber += 1
#             startArray = calcListFromOneNumberNew(changingNumber, startArray, indexToChange)
#         if not arrayIsDESC(startArray):
#             indexToChange+=1
#             if len(startArray) > indexToChange:
#                 changingNumber = startArray[indexToChange]
#                 changingNumber += 1
#                 startArray = calcListFromOneNumberNew(changingNumber, startArray, indexToChange)
#             else:
#                 break#all is done
#     return output

