import random
with open("data") as file:
    lines = file.readlines()

verschieben = 2
#print(lines[0])
front = lines[0][:-33+verschieben]
#print("[front]",front)
dataAndEnd = lines[0][74:]

datas = dataAndEnd[:-24-verschieben]
#print("[datas]",datas)
end = dataAndEnd[8:]
#print("[end]",end)

#print(front + datas + end,end="")



def generateData():
    lis =[]
    datasNeeded = 2
    for x in range(datasNeeded):
        for i in range(1,101):
            lis.append(i)

    random.shuffle(lis)
    strin = ""
    for x in range(datasNeeded):
        strin += str(lis[0])+","
        lis.pop(0)
    #print(lis)


    return strin




intt = 1
for l in lines:
    myDatas = generateData()
    print(front +str(intt)+","+ myDatas + end,end="")
    intt+=1;
