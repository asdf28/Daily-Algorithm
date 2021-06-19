import sys
import math

MX = 123456
N = -1
cnt = 0

li = [True] * (2 * MX + 1)

li[0] = False
li[1] = False

for i in range(2, int(math.sqrt(MX*2))+1):
    j = 2
    while i*j <= MX * 2:
        li[i*j] = False
        j += 1

while True:
    N = int(sys.stdin.readline().rstrip())

    if N == 0:
        break

    for i in range(N+1, 2*N+1):
        if li[i]:
            cnt += 1
    print(cnt)
    cnt = 0
