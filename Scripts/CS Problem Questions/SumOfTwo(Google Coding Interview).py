ar = [3,21,9]
br = [70,18,1]



def hasSumInTheArrays(target):
    for a in ar:
        toLookFor = target-a
        if toLookFor in br:
            return True
    #loop ended
    return False

boooool = hasSumInTheArrays(91)
print(boooool)
# O(n)