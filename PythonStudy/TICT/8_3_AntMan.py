import sys


def solution():
    N = int(sys.stdin.readline().rstrip())
    stock = list(map(int, sys.stdin.readline().split()))

    dp = [0] * (N+1)

    dp[0] = stock[0]
    dp[1] = stock[1]

    for i in range(2, N):
        dp[i] = max(dp[i-1], stock[i] + dp[i-2])

    return dp[N-1]


print(solution())