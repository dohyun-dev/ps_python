from heapq import heappush, heappop, heapify
from collections import defaultdict

def prim(start):
    q = [*graph[start]]
    visited = [False] * (V + 1)
    visited[start] = True
    answer = 0
    heapify(q)

    while q:
        cost, node = heappop(q)

        if visited[node]:
            continue
        visited[node] = True
        answer += cost
        for next_cost, next in graph[node]:
            if visited[next]:
                continue
            heappush(q, (next_cost, next))
    return answer

V, E = map(int, input().split())
graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
print(prim(1))