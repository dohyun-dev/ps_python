import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if arr[i] <= arr[j]:
            continue
        dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))