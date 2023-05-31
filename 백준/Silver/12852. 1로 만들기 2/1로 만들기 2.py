N = int(input())
dp, pre = [0] * (N + 1), [[1]] * (N + 1)
for i in range(2, N + 1):
    dp[i], pre[i] = dp[i-1], pre[i-1]
    if i % 2 == 0 and dp[i//2] < dp[i]:
        dp[i], pre[i] = dp[i//2], pre[i//2]
    if i % 3 == 0 and dp[i//3] < dp[i]:
        dp[i], pre[i] = dp[i//3], pre[i//3]
    dp[i], pre[i] = dp[i] + 1, [i] + pre[i]
print(dp[N])
print(*pre[N])