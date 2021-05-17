import sys


def getresult(diff):
    n = 1
    ans = 0
    while True:
        ans += 1
        if n*n >= diff:
            return ans
        ans += 1
        if n*(n+1) >= diff:
            return ans
        n += 1


T = int(sys.stdin.readline().rstrip())

for i in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    dif = y - x

    print(getresult(dif))
