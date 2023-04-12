from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

for i in range(1, N+1):
    for c in combinations(nums, i):
        if sum(c) == M:
            answer += 1
print(answer)