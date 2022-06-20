import sys


def solution():
    N = int(sys.stdin.readline().rstrip())

    dp = [0] * (N+1)

    dp[0] = 1
    dp[1] = 3

    for i in range(2,N):
        dp[i] = (2*dp[i-2] + dp[i-1]) % 796796

    return dp[N-1]


print(solution())