def calc(x):
    return (x + 1)

N, K = map(int, input().split())
left, right = 0, N
while left <= right:
    col = (left + right) // 2
    row = N - col
    result = calc(col) * calc(row)
    if result < K:
        left = col + 1
    elif result > K:
        right = col - 1
    else:
        print("YES")
        break
else:
    print("NO")