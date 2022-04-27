def getSolution(n):
    toReturn = 0
    for i in range(1,n+1):
        toReturn+=i
    print(toReturn,end=", ")
    return toReturn

for x in range(50):
    if getSolution(x) > 200:
        break

