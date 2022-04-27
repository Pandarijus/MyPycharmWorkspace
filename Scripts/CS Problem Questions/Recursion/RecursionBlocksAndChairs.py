def solution(n):
    if n < 2:
        return 1
    else:
        return solution(n-1)+ solution(n-2)

s = solution(5)
print(s)