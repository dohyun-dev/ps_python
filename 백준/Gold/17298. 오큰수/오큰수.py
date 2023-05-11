N = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1] * N

for idx, num in enumerate(arr):
    while stack and stack[-1][1] < num:
        i, value = stack.pop()
        answer[i] = num
    stack.append((idx, num))
print(*answer)