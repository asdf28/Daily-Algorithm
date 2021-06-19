import sys

num = int(sys.stdin.readline().strip())

for i in range(1, num+1):
    a, b = map(int, sys.stdin.readline().strip().split())
    print("Case #%d: %d + %d = %d" % (i, a, b, a+b))
