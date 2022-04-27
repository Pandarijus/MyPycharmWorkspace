def solution(n):
    if n == 0:
        return 0
    else:
        return n + solution(n-1)

s =solution(6)
print(s)