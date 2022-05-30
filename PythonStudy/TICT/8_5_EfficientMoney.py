import sys
N,M = map(int, sys.stdin.readline().split())

money = []
dp = [-1] * M
for i in range(N):
    money[i] = int(sys.stdin.readline().rstrip())

dp[min(money)-1] = 1