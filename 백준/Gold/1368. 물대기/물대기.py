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


N = int(input())
costs = [[0] * (N + 1) for i in range(N + 1)]
edges = []
parent = [i for i in range(N + 1)]
answer = 0

for i in range(1, N + 1):
    edges.append((0, i, int(input())))

for i in range(1, N + 1):
    for j, num in enumerate(map(int, input().split()), 1):
        if i == j:
            continue
        edges.append((i, j, num))
edges.sort(key=lambda x: x[2])

for a, b, cost in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    answer += cost
print(answer)