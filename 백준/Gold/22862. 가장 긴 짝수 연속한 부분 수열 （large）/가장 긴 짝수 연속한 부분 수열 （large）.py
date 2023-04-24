N, K = map(int, input().split())
arr = list(map(int, input().split()))
left, right, odd = 0, 0, 0
answer = 0
while right < N:
    if odd <= K:
        if arr[right] % 2:
            odd += 1
        answer = max(answer, right - left - odd + 1)
        right += 1
    else:
        while odd > K:
            if arr[left] % 2:
                odd -= 1
            left += 1
print(answer)