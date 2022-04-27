def solution(x, y):
    triangularNumber = x-1 + y-1
    theSolution = getSolution(triangularNumber) + x
    return str(theSolution)


def getSolution(n):
    toReturn = 0
    for i in range(1,n+1):
        toReturn+=i
    return toReturn

s =solution(100000,100000)
print(s)
#     iD = 1
#     dic = {(1,1):iD}
#     #for up in range(2,max(x,y)+2):
#     up = 1
#     yPos = up
#     xPos = 1
#     while max(xPos,yPos) <= 100000 and min(xPos,yPos)>=1:
#         up+=1
#         yPos = up
#         xPos = 1
#         iD += 1
#         dic[(xPos, yPos)] = iD
#         #print(up)
#         while yPos > 1:
#             iD+=1
#             yPos-=1
#             xPos+=1
#             dic[(xPos,yPos)] = iD
#             if xPos==x and yPos == y:
#                 printPyra(dic,x,y)
#                 return iD
#
#
# def printPyra(dic,x,y):
#     #print(dic)
#     for xx in range(1,x+1):
#         print()
#         for yy in range(1, y+1):
#             print((xx,yy),dic[(xx,yy)], end=" ")



# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10

#(1,4)
#(1,3)(2,3)
#(1,2)(2,2)(3,2)
#(1,1)(2,1)(3,1)(4,1)

#y up x same
#y up x same,y down x up,
#stay
# s = solution(4,4)
# print()
# print("SOLUTION:",s)