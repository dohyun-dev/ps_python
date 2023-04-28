N = int(input())
left, right = 0, N
answer = 0

while left <= right:
    mid = (left + right) // 2
    if mid ** 2 < N:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1
print(answer)