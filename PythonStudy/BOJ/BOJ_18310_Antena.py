import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

print(arr[(len(arr) - 1)//2])