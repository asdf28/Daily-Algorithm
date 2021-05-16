import sys


def getresult(diff):
    ans = 2
    tmp = 2
    cnt = 1
    if diff == 1:
        return 1
    else:
        while True:
            for j in range(cnt):
                if tmp > diff:
                    return ans-1
                tmp += cnt
                ans += 1
            cnt += 1


T = int(sys.stdin.readline().rstrip())

for i in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    dif = y - x

    print(getresult(dif))
