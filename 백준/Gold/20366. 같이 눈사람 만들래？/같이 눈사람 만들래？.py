N = int(input())
arr = sorted(list(map(int, input().split())))
check = [False] * N
answer = float("inf")

for i in range(N):
    for j in range(i+1, N):
        left_snowman = arr[i] + arr[j]
        left, right = 0, N-1
        check[i], check[j] = True, True
        while left < right:
            if check[left]:
                left += 1
                continue
            if check[right]:
                right -= 1
                continue
            right_snowman = arr[left] + arr[right]
            answer = min(answer, abs(left_snowman - right_snowman))
            if left_snowman <= right_snowman:
                right -= 1
            else:
                left += 1
        check[i], check[j] = False, False
print(answer)