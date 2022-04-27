
waters = []
sea = []
def start():
    for x in range(0, len(twoDArray)):
        for y in range(0, len(twoDArray[0])):
            print(str(x)+'|'+str(y))
            checkPos(x,y,False)



def checkPos(x,y,isRiver):

    if twoDArray[x][y]== 1:
        twoDArray[x][y] = 2#found water
        waters.append((x, y))
        if not isRiver:#start breth first search if first found
            checkAdjacent(x, y)
            print(waters)
            print(len(waters))
            sea.append(waters.copy())
            waters.clear()
        else:
            checkAdjacent(x,y)


def checkAdjacent(x,y):
    for addPos in adjacentPositions:
        newX = x + addPos[0]
        newY = y + addPos[1]
        if isValidPosition(newX,newY):
            checkPos(newX, newY, True)


def isValidPosition(x,y):
    return 0 <= x < len(twoDArray) and 0 <= y < len(twoDArray[0])


twoDArray = [
[0,1,1,1,1,1,0],
[0,1,0,0,0,0,1],
[0,0,1,1,1,1,0],
[0,0,1,0,0,1,1],
[0,0,0,0,0,0,0],
[1,1,1,1,0,1,1],
[1,0,0,0,0,1,0],
[1,1,0,1,1,1,0],
]

adjacentPositions = [(1,0),(-1,0),(0,1),(0,-1)]

start()
print(twoDArray)
print(sea)
print(len(sea))
