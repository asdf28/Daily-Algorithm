import sys

N = int(sys.stdin.readline().rstrip())
cmp = N
cycle = 0

while True:
    cmp = (cmp//10 + cmp % 10) % 10 + (cmp % 10) * 10
    cycle += 1
    if cmp == N:
        print(cycle)
        break
