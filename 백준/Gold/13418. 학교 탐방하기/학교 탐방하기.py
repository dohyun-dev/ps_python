def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for _ in range(M + 1)], key=lambda x: -x[2])
parent = [i for i in range(N + 1)]
max_total, min_total = 0, 0

for a, b, cost in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    min_total += 1 if cost == 0 else 0

edges.sort(key=lambda x: x[2])
parent = [i for i in range(N + 1)]
for a, b, cost in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    max_total += 1 if cost == 0 else 0

print(max_total ** 2 - min_total ** 2)