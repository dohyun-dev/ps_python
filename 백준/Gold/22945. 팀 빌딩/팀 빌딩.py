N = int(input())
developer = list(map(int, input().split()))
left, right = 0, N - 1
answer = 0
while left < right:
    cur = (right - left - 1) * min(developer[left], developer[right])
    answer = max(answer, cur)
    if developer[left] > developer[right]:
        right -= 1
    else:
        left += 1
print(answer)