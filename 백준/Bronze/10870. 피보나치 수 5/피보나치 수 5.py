N = int(input())
dp = [0, 1]
for i in range(2, N+1):
    dp.append(dp[i-1] + dp[-2])
print(dp[N])