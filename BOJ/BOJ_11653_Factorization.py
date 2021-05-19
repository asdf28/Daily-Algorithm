import sys

N = int(sys.stdin.readline().rstrip())
ans = []

fact = 2

while True:
    if N == 1:
        break
    if N % fact == 0:
        N //= fact
        print(fact)
        fact = 2
    else:
        fact += 1
