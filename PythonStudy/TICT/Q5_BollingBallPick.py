import sys

N,M = map(int, sys.stdin.readline().split())

ball = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if ball[i] != ball[j]:
            cnt += 1

print(cnt)