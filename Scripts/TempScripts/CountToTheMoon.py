dic = {}
numb = 10
for i in range(1,numb+1):
    for j in range(1,numb+1):
        _ = i*j
        if _ not in dic:
            dic[_] = 1
        else:
            dic[_] += 1
        #print(str(_)+"",end="/")
    #print(f"\n-----[{i}]-----")

lis = sorted((value,key)for (key,value) in dic.items())
lis.reverse()
print(lis)
