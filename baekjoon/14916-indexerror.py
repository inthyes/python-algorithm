import sys
N = int(sys.stdin.readline())
dp = [0] * (N+1)
dp[2] = 1
dp[5] = 1
for i in range(3, N+1):
    if dp[i-2] != 0:
        dp[i] = dp[i-2] + 1
    if dp[i-5] != 0:
        dp[i] = min(dp[i-5] + 1, dp[i])
if dp[N] == 0:
    print(-1)
print(dp[N])
