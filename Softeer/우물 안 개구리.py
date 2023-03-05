import sys

N, M = map(int, input().split())
weights = list(map(int, input().split()))
check = [True] * N

for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    if weights[a] > weights[b]:
        check[b] = False
    elif weights[a] < weights[b]:
        check[a] = False
    else:
        check[a], check[b] = False, False
print(check.count(True))