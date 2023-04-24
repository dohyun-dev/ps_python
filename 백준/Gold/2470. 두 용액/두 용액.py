N = int(input())
arr = sorted(list(map(int, input().split())))
left, right = 0, N - 1
total, answer = float("inf"), []

while left < right:
    left_val, right_val = arr[left], arr[right]
    if abs(left_val + right_val) < total:
        total = abs(left_val + right_val)
        answer = [left_val, right_val]
        if total == 0:
            break
    if left_val + right_val < 0:
        left += 1
    else:
        right -= 1
print(*answer)