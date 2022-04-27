temp = 0
n = 3
prevTemp = 0
for i in range(1,10+1):
    temp += pow(n,i)
    print(temp,end="  ")
    #print("/3: "+str(int(temp/3)))
    #div = temp/prevTemp
    dif = temp-prevTemp
    prevTemp = temp
    #print(div)
    print(dif)


s = temp
print("Solution: "+str(s))