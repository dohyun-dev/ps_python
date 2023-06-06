N = int(input())
meetings = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 2)

for day in range(N, 0, -1):
    period, profit = meetings[day]
    if day + period >= N + 2:
        dp[day] = dp[day + 1]
    else:
        dp[day] = max(dp[day + 1], dp[day + period] + profit)

print(dp[1])