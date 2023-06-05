N = int(input())

MOD = 1000000000

dp = [
    [0] * 10,
    [0] + ([1] * 9)
]

for i in range(2, N+1):
    dp.append([0] * 10)
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N]) % MOD)