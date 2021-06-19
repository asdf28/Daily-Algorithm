import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for e in A:
    if e < X:
        print(e, end=" ")
