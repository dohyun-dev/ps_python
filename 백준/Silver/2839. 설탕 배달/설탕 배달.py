N = int(input())
dp = [-1] * (N + 1)
dp[0] = 0
for i in range(3, N+1):
    if dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
    if dp[i-5] != -1:
        dp[i] = dp[i-5] + 1
print(dp[N])