def solve(firstString,secondString,a,b,savedDic={}):
    #print(a,b)
    if (a, b) in savedDic:
        return savedDic[(a, b)]
    else:
        if len(firstString) == a or len(secondString)==b:
            return ""
        if firstString[a] == secondString[b]:
            toReturn =firstString[a]+ solve(firstString,secondString,a+1,b+1,savedDic)
            savedDic[(a, b)] = toReturn
            return toReturn
        else:
            pathA = solve(firstString,secondString,a+1,b,savedDic)
            pathB = solve(firstString,secondString,a,b+1,savedDic)
            if len(pathA) > len(pathB):
                savedDic[(a, b)] = pathA
                return pathA
            else:
                savedDic[(a, b)] = pathB
                return pathB
        #check 2 paths if they are equal to the next char

    #print(firstString[1:5])# [i,j]
    # the char at index i is the first char of the new substring
    #j is the char that is not in the string.
    # so i is inclusive and j isn't.     i<= charsIndexThatGetInTheString < j
    #my code should check if the chars are equal if so hard code it

s = solve("When did you come home?", "When where you home?",0,0,{})
print(s)
#"Hello!!!!","Yellow" = ello
#"When did you come home?" "When where you home?" = When you home?
#h != y