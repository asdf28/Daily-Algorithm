import sys

N = sys.stdin.readline().rstrip()
ARR = list(map(int, sys.stdin.readline().rstrip().split()))

print(min(ARR), max(ARR))