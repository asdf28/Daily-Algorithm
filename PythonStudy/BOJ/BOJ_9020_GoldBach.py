import sys
import math

T = int(sys.stdin.readline().rstrip())

li = [True] * (10000 + 1)

li[0] = False
li[1] = False

for i in range(2, int(math.sqrt(10000))+1):
    j = 2
    while i*j <= 10000:
        li[i*j] = False
        j += 1

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    i = N // 2
    while True:
        if li[i]:
            if li[N-i]:
                print(N - i, i)
                break
        i += 1