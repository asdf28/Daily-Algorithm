import sys
num = int(input())

for i in range(1, num+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
