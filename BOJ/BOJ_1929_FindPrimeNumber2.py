import sys
import math

N, M = map(int, sys.stdin.readline().rstrip().split())

li = [True]*(M+1)

li[0] = False
li[1] = False

for i in range(2, int(math.sqrt(M))+1):
    j = 2
    while i*j <= M:
        li[i*j] = False
        j += 1

for i in range(N, M+1):
    if li[i]:
        print(i)
