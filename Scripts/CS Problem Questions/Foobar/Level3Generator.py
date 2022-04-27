def solution(n):
    dicStairs = {3:[[2,1]],4:[[3,1]]}#5:[[4,1],[3,2]]
    currStairs = []
    addorialDic = createAdorialDic()

    while n not in dicStairs:
        for i in range(5, n + 1):
            #print(i)
            prevStairs = dicStairs[i-1]
            #print(prevStairs)
            for stair in prevStairs:
                #print(i,"INDEX",stair)
                for index in range(len(stair)):#for height in stair:
                    #print(i,"INDEX",index)
                    newStair = stair.copy()
                    newStair[index] +=1

                    if stairIsValid(newStair,index,currStairs):
                        currStairs.append(newStair)


            #AT THE END OF MY CODE
            if i in addorialDic:
                currStairs.append(addorialDic[i])
            dicStairs[i] = currStairs.copy()  # fit this in somewhere
            currStairs.clear()

    return dicStairs





def stairIsValid(stair,index,currStairs):
    if len(stair) - 1 > index:#check if can move one index up (array bounds)
        if stair[index + 1] == stair[index]:
            return False
    if index > 0:#check if can move one index down (array bounds)
        if stair[index - 1] == stair[index]:
            return False
    if stair in currStairs:#check if value is already in array
        return False
    #If didn't step on landmine:
    return True#Else

def createAdorialDic():
    dic = {}
    for a in range(2,50):
        key,array = getAddorialArray(a)
        if key > 200:
            break
        else:
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
    return add,steps


s = solution(50)
values = list(s.values())
for i in range(len(values)):
    print("-----------",i+3,"----------")
    print()
    print(values[i])
    print()
# pev= 1
# rprevD= 0
# for i in range(len(values)):
#     L = len(values[i])
#     D = L-prev
#     P = D-prevD
#     print("(",i+3,"L=",L,")","D=",D,"P=",P)   #,values[i],end="\n")
#     prevD = D
#     prev = L

#print(s)


























# def recursion(n):
#     if n < 3:
#         return 0
#     elif n == 3 or n == 4:
#         return 1



#s(n)  n >=2





#Solution.solution(3)=1
#Solution.solution(200) = 487067745