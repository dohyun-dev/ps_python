# kruskal algo
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

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
answer = 0
edges = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])

for a, b, cost in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    answer += cost

print(answer)