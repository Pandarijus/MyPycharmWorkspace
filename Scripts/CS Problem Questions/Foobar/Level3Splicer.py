a = [0, 1, 1, 2, 2]

diffs = []
for i in range(len(a)-1):
    diff = a[i+1]-a[i]
    diffs.append(diff)
print(diffs)




# Starts at: N= 3 []= 2 C= 1
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# Starts at: N= 6 []= 3 C= 1
# [1, 1, 2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 19, 21, 24, 27, 30, 33, 37, 40, 44, 48, 52, 56, 61, 65, 70, 75, 80, 85, 91, 96, 102, 108, 114, 120, 127, 133, 140, 147, 154, 161, 169, 176, 184]
# [0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3, 2, 3, 3, 3, 3, 4, 3, 4, 4, 4, 4, 5, 4, 5, 5, 5, 5, 6, 5, 6, 6, 6, 6, 7, 6, 7, 7, 7, 7, 8, 7, 8]
# [1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1]
# Starts at: N= 10 []= 4 C= 1
# [1, 1, 2, 3, 5, 6, 9, 11, 15, 18, 23, 27, 34, 39, 47, 54, 64, 72, 84, 94, 108, 120, 136, 150, 169, 185, 206, 225, 249, 270, 297, 321, 351, 378, 411, 441, 478, 511, 551, 588, 632]
# [0, 1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 7, 5, 8, 7, 10, 8, 12, 10, 14, 12, 16, 14, 19, 16, 21, 19, 24, 21, 27, 24, 30, 27, 33, 30, 37, 33, 40, 37, 44]
# [1, 0, 1, -1, 2, -1, 2, -1, 2, -1, 3, -2, 3, -1, 3, -2, 4, -2, 4, -2, 4, -2, 5, -3, 5, -2, 5, -3, 6, -3, 6, -3, 6, -3, 7, -4, 7, -3, 7]
# Starts at: N= 15 []= 5 C= 1
# [1, 1, 2, 3, 5, 7, 10, 13, 18, 23, 30, 37, 47, 57, 70, 84, 101, 119, 141, 164, 192, 221, 255, 291, 333, 377, 427, 480, 540, 603, 674, 748, 831, 918, 1014, 1115]
# [0, 1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 10, 10, 13, 14, 17, 18, 22, 23, 28, 29, 34, 36, 42, 44, 50, 53, 60, 63, 71, 74, 83, 87, 96, 101]
# [1, 0, 1, 0, 1, 0, 2, 0, 2, 0, 3, 0, 3, 1, 3, 1, 4, 1, 5, 1, 5, 2, 6, 2, 6, 3, 7, 3, 8, 3, 9, 4, 9, 5]
# Starts at: N= 21 []= 6 C= 1
# [1, 1, 2, 3, 5, 7, 11, 14, 20, 26, 35, 44, 58, 71, 90, 110, 136, 163, 199, 235, 282, 331, 391, 454, 532, 612, 709, 811, 931, 1057]
# [0, 1, 1, 2, 2, 4, 3, 6, 6, 9, 9, 14, 13, 19, 20, 26, 27, 36, 36, 47, 49, 60, 63, 78, 80, 97, 102, 120, 126]
# [1, 0, 1, 0, 2, -1, 3, 0, 3, 0, 5, -1, 6, 1, 6, 1, 9, 0, 11, 2, 11, 3, 15, 2, 17, 5, 18, 6]
# Starts at: N= 28 []= 7 C= 1
# [1, 1, 2, 3, 5, 7, 11, 15, 21, 28, 38, 49, 65, 82, 105, 131, 164, 201, 248, 300, 364, 436, 522]
# [0, 1, 1, 2, 2, 4, 4, 6, 7, 10, 11, 16, 17, 23, 26, 33, 37, 47, 52, 64, 72, 86]
# [1, 0, 1, 0, 2, 0, 2, 1, 3, 1, 5, 1, 6, 3, 7, 4, 10, 5, 12, 8, 14]
# Starts at: N= 36 []= 8 C= 1
# [1, 1, 2, 3, 5, 7, 11, 15, 22, 29, 40, 52, 70, 89, 116]
# [0, 1, 1, 2, 2, 4, 4, 7, 7, 11, 12, 18, 19, 27]
# [1, 0, 1, 0, 2, 0, 3, 0, 4, 1, 6, 1, 8]
# Starts at: N= 45 []= 9 C= 1
# [1, 1, 2, 3, 5, 7]
# [0, 1, 1, 2, 2]
# [1, 0, 1, 0]