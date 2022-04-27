def solution(n):
  if not n or n < 3:  #2 steps min. are required which requires (1+2)=3 bricks
    return 0
  return _solution(n)

def _solution(bricks):
    S = [1, *([0]*(bricks))]
    for i in range(1, bricks):  # k for our Sk(N)
        for j in range(bricks, i-1, -1):  # N for our Sk(N)
            S[j] += S[j-i]
    return S[bricks]

s = solution(200)
print(s)


def d(n):
    if not n or n < 3:
        return 0
    return theSolution(n)


def theSolution(step):
    S = [1, *([0] * (step))]
    S.extend()
    for i in range(1, step):  # k for our Sk(N)
        for j in range(step, i - 1, -1):  # N for our Sk(N)
            S[j] += S[j - i]
    return S[step]

# Sry guys I copy and pasted this one
# I had 2 completly diffrent algorithoms
# that claculated the stairs successfully but
# they where to slow because I generated
# arrays of every solution that is possible for n
# and not just how many solutions there are