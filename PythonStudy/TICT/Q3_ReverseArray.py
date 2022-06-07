import sys

arr = list(map(int, sys.stdin.readline().rstrip()))
ans = []

zero = [0] * len(arr)
one = [1] * len(arr)

prev = -1
cnt_zero = 0
for i in range(len(arr)):
    if prev != arr[i] and arr[i] != zero[i]:
        prev = arr[i]
        cnt_zero += 1
    prev = arr[i]

cnt_one = 0
for i in range(len(arr)):
    if prev != arr[i] and arr[i] != one[i]:
        prev = arr[i]
        cnt_one += 1
    prev = arr[i]

print(min(cnt_one,cnt_zero))