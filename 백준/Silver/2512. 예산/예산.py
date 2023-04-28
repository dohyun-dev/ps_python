N, arr = int(input()), list(map(int, input().split()))
limit = int(input())
left, right = 0, max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(min(mid, num) for num in arr)
    if total <= limit:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)