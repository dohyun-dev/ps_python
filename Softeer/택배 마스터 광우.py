import sys
from itertools import permutations

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = float("inf")

for p in permutations(arr):
    total, ptr = 0, 0
    for _ in range(K):
        tmp = 0
        while tmp + p[ptr] <= M:
            tmp += p[ptr]
            ptr = (ptr + 1) % N
        total += tmp
    answer = min(answer, total)
print(answer)