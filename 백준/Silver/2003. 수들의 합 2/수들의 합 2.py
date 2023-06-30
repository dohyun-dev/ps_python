N, M = map(int, input().split())
arr = list(map(int, input().split()))
left, total, answer = -1, 0, 0
for right in range(N):
    total += arr[right]
    while left < right and M < total:
        left += 1
        total -= arr[left]
    if total == M:
        answer += 1
print(answer)