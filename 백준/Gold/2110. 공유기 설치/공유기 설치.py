N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
left, right = 0, 10 ** 9

while left <= right:
    mid = (left + right) // 2
    check = [False] * N
    total = 0

    for i in range(N):
        if check[i]:
            continue
        for j in range(i, N):
            if arr[j] > arr[i] + mid:
                break
            check[j] = True
        total += 1
    if total < C:
        right = mid - 1
    else:
        left = mid + 1
print(left)