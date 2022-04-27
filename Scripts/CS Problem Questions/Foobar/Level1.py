def solution(area):
    if 0 < area <= 1000000:
        solutionList = []
        squares = []
        x = 1
        square = x*x
        while square <= area:
            squares.append(square)
            x+=1
            square = x*x
        #end while
        #print("StartArea:",area)
        #print(*squares)
        leftOverArea = area
        i = -1
        while leftOverArea > 0:
            while leftOverArea >= squares[i]:
                areaToCutAway = squares[i]
                leftOverArea -= areaToCutAway
                solutionList.append(areaToCutAway)
            else:
                i-=1
        else:
            #print(*solutionList)
            return solutionList
    else:
        return None
