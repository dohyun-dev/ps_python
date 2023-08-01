def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
location = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N + 1)]
edges = []
answer = 0

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        x1, y1 = location[i]
        x2, y2 = location[j]
        dist = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
        edges.append((dist, i, j))

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

edges.sort()

for dist, a, b in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    answer += dist

print('{:.2f}'.format(answer))