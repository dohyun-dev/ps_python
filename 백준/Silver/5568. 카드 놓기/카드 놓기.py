from itertools import permutations

N, K = int(input()), int(input())
cards = [input() for _ in range(N)]
result = set()
for combi in permutations(cards, K):
    tmp = ""
    for c in combi:
        tmp += c
    result.add(tmp)
print(len(result))