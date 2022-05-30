import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * n

dp[0] = 1
dp[1] = 3

for i in range(2,n):
    dp[i] = ( dp[i-1] + (2 * dp[i-2]) ) % 796796

print(dp[n-1])