import sys

n = int(sys.stdin.readline().rstrip())

arr = []

for i in range(n):
    tmp = sys.stdin.readline().split()
    arr.append((tmp[0], int(tmp[1])))

arr.sort(key=lambda x: x[1])

for i in range(n):
    print(arr[i][0])