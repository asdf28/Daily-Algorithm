import sys


def solution():
    N = int(sys.stdin.readline().rstrip())
    dp = [0] * (N+1)

    dp[0] = 0
    dp[1] = 0

    for i in range(2, N+1):
        dp[i] = dp[i - 1] + 1

        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

    return dp[N]


print(solution())