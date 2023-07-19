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
edges = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x: (x[2], x[0], x[1]))
answer = 0

for node1, node2, cost in edges:
    if find(node1) != find(node2):
        union(node1, node2)
        answer += cost
print(answer)