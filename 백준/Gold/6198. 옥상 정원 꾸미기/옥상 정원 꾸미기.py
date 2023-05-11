n = int(input())
arr = [int(input()) for _ in range(n)]
answer = 0
stack = []
for a in arr:
    while stack and stack[-1] <= a:
        stack.pop()
    stack.append(a)
    answer += len(stack) - 1
print(answer)