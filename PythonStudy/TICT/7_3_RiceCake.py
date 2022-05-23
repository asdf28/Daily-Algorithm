import sys

N, M = map(int,sys.stdin.readline().split())

riceCakes = list(map(int,sys.stdin.readline().split()))

left = 0
right = max(riceCakes)

while left <= right:
    mid = (left + right) // 2

    total = 0;

    for i in range(N):
        if riceCakes[i] > mid:
            total += riceCakes[i] - mid
    if total == M:
        result = mid
        break

    if total > M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)