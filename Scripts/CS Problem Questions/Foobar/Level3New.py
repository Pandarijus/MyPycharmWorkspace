def solution(n):
    maxStairLenght = getWhatTheMaxWidthOfAStairIs(n)
    dic = getDic(maxStairLenght)
    everyStartArray = getEveryStartArray(n,maxStairLenght,dic)

    return getSolution(everyStartArray)

def getSolution(everyStartArray):
    output = []

    for startArray in everyStartArray:
        line = generateArray(startArray)
        if len(startArray) == 9:
            c = len(line)
            if len(save)==0:
                print()
                print("Starts at:","N=", sum(startArray), "[]=", len(startArray),"C=",c)

            save.append(c)
            #print()
        #print(line)

        output.extend(line)
    return output

#--------------------------------------------------------------------------
#prev = 0










def generateArray(array):
    output = []
    l = len(array)
    if l == 2:
        while array[0] > array[1]:
            output.append(array.copy())
            array[0] -= 1
            array[1] += 1
        return output#Quit
    else:
        while True:
            output.append(array.copy())
            array[0] -= 1
            array[1] += 1
            if array[0] <= array[1]:
                couldNotFindValidArray = True
                for i in range(2,l):
                    array = gen(array,i)
                    if arrayIsDESC(array):
                        couldNotFindValidArray = False
                        break
                if couldNotFindValidArray:
                    #print("END:",l)
                    return output  # Quit




def gen(array,indexToChange):
    n = sum(array)
    l = len(array)
    sub = array[indexToChange:]
    sub[0]+=1
    sub.reverse()

    r = l-len(sub)-1
    for j in range(r):
        sub.append(sub[-1]+1)

    biggest = n - sum(sub)
    sub.append(biggest)
    sub.reverse()
    # print("Generated List:",sub)
    return sub




#--------------------------------------------------------------------------









def arrayIsDESC(array):

    for i in range(len(array)-1):
        if array[i]<=array[i+1]:# if left is smaller than right :[1,5]
            #print(array,"NO")
            return False
    #print(array,"Yes")
    return True





def getEveryStartArray(n,maxStairLenght,dic):
    everyStartArray = []
    for m in range(2,maxStairLenght+1):
        startArray = getStartArray(n, m, dic)
        everyStartArray.append(startArray)
    return everyStartArray

def getStartArray(n, l, dic):
    l -=1
    su = sum(list(dic[l]))
    startNumber = n- su
    startArray = [startNumber]
    startArray.extend(dic[l])
    #print("StartArray:",startArray)
    return startArray


def getWhatTheMaxWidthOfAStairIs(n):
    add = 0
    for i in range(1,201):
        add += i
        if add > n:
            index = i-1#prev index
            return index



def getDic(l):
    dic = {}
    for a in range(1,l+1):
        key,array = getAddorialArray(a)
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
    return i,steps #make key 1 bigger so it makes more sence




#s = solution(100)
#print("(",100,")","Lenght:", len(s))
#print("{",end="")


calc = False
save = []
if calc:
    for i in range(167,200):
        s = solution(i)
        print( str(i)+":"+str(len(s)),end=", ")
else:
    for i in range(3, 50+1):
        #print("--------------[Start:", i, "]--------------")
        s = solution(i)

#print("starts at 6 ")
print(save)
#        print()
        #print(s)

        # print("(",i,")","Lenght:", len(s))


#(3-168)#{3:1, 4:1, 5:2, 6:3, 7:4, 8:5, 9:7, 10:9, 11:11, 12:14, 13:17, 14:21, 15:26, 16:31, 17:37, 18:45, 19:53, 20:63, 21:75, 22:88, 23:103, 24:121, 25:141, 26:164, 27:191, 28:221, 29:255, 30:295, 31:339, 32:389, 33:447, 34:511, 35:584, 36:667, 37:759, 38:863, 39:981, 40:1112, 41:1259, 42:1425, 43:1609, 44:1815, 45:2047, 46:2303, 47:2589, 48:2909, 49:3263, 50:3657, 51:4096, 52:4581, 53:5119, 54:5717, 55:6377, 56:7107, 57:7916, 58:8807, 59:9791, 60:10879, 61:12075, 62:13393, 63:14847, 64:16443, 65:18199, 66:20131, 67:22249, 68:24575, 69:27129, 70:29926, 71:32991, 72:36351, 73:40025, 74:44045, 75:48445, 76:53249, 77:58498, 78:64233, 79:70487, 80:77311, 81:84755, 82:92863, 83:101697, 84:111321, 85:121791, 86:133183, 87:145577, 88:159045, 89:173681, 90:189585, 91:206847, 92:225584, 93:245919, 94:267967, 95:291873, 96:317787, 97:345855, 98:376255, 99:409173,100:444792, 101:483329, 102:525015, 103:570077, 104:618783, 105:671417, 106:728259, 107:789639, 108:855905, 109:927405, 110:1004543, 111:1087743, 112:1177437, 113:1274117, 114:1378303, 115:1490527, 116:1611387, 117:1741520, 118:1881577, 119:2032289, 120:2194431,121:2368799, 122:2556283, 123:2757825, 124:2974399, 125:3207085, 126:3457026, 127:3725409, 128:4013543, 129:4322815, 130:4654669, 131:5010687, 132:5392549, 133:5802007, 134:6240973, 135:6711479, 136:7215643, 137:7755775, 138:8334325, 139:8953855, 140:9617149, 141:10327155, 142:11086967, 143:11899933, 144:12769601, 145:13699698, 146:14694243, 147:15757501, 148:16893951, 149:18108417, 150:19406015,151:20792119, 152:22272511, 153:23853317,154:25540981, 155:27342420,156:29264959, 157:31316313, 158:33504745, 159:35839007, 160:38328319, 161:40982539, 162:43812109, 163:46828031, 164:50042055, 165:53466623, 166:57114843,167:61000703, 168:65139007

#200:487067745



#dic ={3:1, 4:1, 5:2, 6:3, 7:4, 8:5, 9:7, 10:9, 11:11, 12:14, 13:17, 14:21, 15:26, 16:31, 17:37, 18:45, 19:53, 20:63, 21:75, 22:88, 23:103, 24:121, 25:141, 26:164, 27:191, 28:221, 29:255, 30:295, 31:339, 32:389, 33:447, 34:511, 35:584, 36:667, 37:759, 38:863, 39:981, 40:1112, 41:1259, 42:1425, 43:1609, 44:1815, 45:2047, 46:2303, 47:2589, 48:2909, 49:3263, 50:3657, 51:4096, 52:4581, 53:5119, 54:5717, 55:6377, 56:7107, 57:7916, 58:8807, 59:9791, 60:10879, 61:12075, 62:13393, 63:14847, 64:16443, 65:18199, 66:20131, 67:22249, 68:24575, 69:27129, 70:29926, 71:32991, 72:36351, 73:40025, 74:44045, 75:48445, 76:53249, 77:58498, 78:64233, 79:70487, 80:77311, 81:84755, 82:92863, 83:101697, 84:111321, 85:121791, 86:133183, 87:145577, 88:159045, 89:173681, 90:189585, 91:206847, 92:225584, 93:245919, 94:267967, 95:291873, 96:317787, 97:345855, 98:376255, 99:409173,100:444792, 101:483329, 102:525015, 103:570077, 104:618783, 105:671417, 106:728259, 107:789639, 108:855905, 109:927405, 110:1004543, 111:1087743, 112:1177437, 113:1274117, 114:1378303, 115:1490527, 116:1611387, 117:1741520, 118:1881577, 119:2032289, 120:2194431,121:2368799, 122:2556283, 123:2757825, 124:2974399, 125:3207085, 126:3457026, 127:3725409, 128:4013543, 129:4322815, 130:4654669, 131:5010687, 132:5392549, 133:5802007, 134:6240973, 135:6711479, 136:7215643, 137:7755775, 138:8334325, 139:8953855, 140:9617149, 141:10327155, 142:11086967, 143:11899933, 144:12769601, 145:13699698, 146:14694243, 147:15757501, 148:16893951, 149:18108417, 150:19406015,151:20792119, 152:22272511, 153:23853317,154:25540981, 155:27342420,156:29264959, 157:31316313, 158:33504745, 159:35839007, 160:38328319, 161:40982539, 162:43812109, 163:46828031, 164:50042055, 165:53466623, 166:57114843,200:487067745}

# #print(dic[133])

