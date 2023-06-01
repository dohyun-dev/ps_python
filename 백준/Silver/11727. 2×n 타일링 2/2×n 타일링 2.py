N = int(input())
dp = [0, 1, 3]
for i in range(3, N+1):
    dp.append((dp[-1] + dp[-2] * 2) % 10007)
print(dp[N])