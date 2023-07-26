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
parent = [i for i in range(N + 1)]
edges = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x: x[2])
selected = []

for a, b, cost in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    selected.append(cost)
print(sum(selected[:-1]))