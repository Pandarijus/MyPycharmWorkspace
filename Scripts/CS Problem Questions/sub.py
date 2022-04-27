def isValidSubsequence(array, sequence):
    s=0
    for i in range(len(array)):
        isSame = sequence[s]==array[i]
        if isSame:
            s+=1
            if s == len(sequence):
                return True#i don't want to overshoot/out of bounds
    return False

so =isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10])
print(so)