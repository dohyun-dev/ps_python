"""
nCr = n-1Cr-1 + n-1Cr
"""
for _ in range(int(input())):
    N, M = map(int, input().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1:
                dp[i][j] = j
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[N][M])