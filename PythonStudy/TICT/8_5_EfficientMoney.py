import sys


def solution():
    N, M = map(int, sys.stdin.readline().split())
    coins = []
    dp = [int(1e9)] * (10000+1)

    for i in range(N):
        coin = int(sys.stdin.readline().rstrip())
        coins.append(coin)
        dp[coin] = 1

    for i in range(1, M+1):
        for coin in coins:
            if i - coin <= 0:
                continue
            dp[i] = min(dp[i-coin]+1, dp[i])

    if dp[M] == int(1e9):
        return -1
    return dp[M]


print(solution())




















# import sys
# N,M = map(int, sys.stdin.readline().split())
#
# money = []
# dp = [-1] * M
# for i in range(N):
#     money[i] = int(sys.stdin.readline().rstrip())
#
# dp[min(money)-1] = 1