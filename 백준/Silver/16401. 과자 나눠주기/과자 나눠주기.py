def calc(cut):
    return sum(stick // cut for stick in sticks)

M, N = map(int, input().split())
sticks = list(map(int, input().split()))
left, right = 1, max(sticks)
while left <= right:
    mid = (left + right) // 2
    if calc(mid) < M:
        right = mid - 1
    else:
        left = mid + 1
print(right)