import sys

num = int(sys.stdin.readline().strip())

for i in range(1, num+1):
    a, b = map(int, sys.stdin.readline().strip().split())
    print("Case #", end="")
    print(i, end="")
    print(": ",end="")
    print(a+b)