def loop(x,y,value,steps):
    if steps > 100:
        return
    else:
        a = 1 if steps%2 == 0 else -1

        under = (x*y)
        #print(under, end = ", ")
        myValue = a/under
        value += myValue
        #print("[",steps,"]","VALUE:     ",value,"            My:", myValue)
        loop(x+1,y+1,value,steps+1)


loop(1,3,0,0)

#1/4 is the anwser

ab = [3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 399, 440, 483, 528, 575, 624, 675, 728, 783, 840, 899, 960, 1023, 1088, 1155, 1224, 1295, 1368, 1443, 1520, 1599, 1680, 1763, 1848, 1935, 2024, 2115, 2208, 2303, 2400, 2499, 2600, 2703]
# abc = []
# for x in range (0,len(ab)-1):
#     diff = ab[x+1]-ab[x]
#     abc.append(diff)
# for c in abc:
#     print(c, end = ", ")

diffs = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103]
#startVelocity = 5
# axeleration = 2
# 2x+5
