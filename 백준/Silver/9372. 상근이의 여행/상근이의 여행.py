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


for _ in range(int(input())):
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    parent = [i for i in range(N + 1)]
    answer = 0

    for a, b in edges:
        if find(a) == find(b):
            continue
        union(a, b)
        answer += 1
    print(answer)