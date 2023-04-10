from itertools import permutations

N, M = map(int, input().split())
nums = list(sorted(map(int, input().split())))
for p in permutations(nums, M):
    print(*p)