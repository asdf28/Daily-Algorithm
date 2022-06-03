import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

max_fear = 0
cnt = 0
result = 0
for i in range(n):
    max_fear = max(max_fear, arr[i])

    cnt += 1

    if cnt == max_fear:
        result += 1
        cnt = 0
        max_fear = 0

print(result)