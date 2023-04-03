from itertools import combinations
from collections import deque

def bfs(chickens):
    q = deque([(0, chickens[0]), (0, chickens[1])])
    dist = [False] * (N+1)
    total = 0

    for c in chickens:
        dist[c] = True

    while q:
        d, cur = q.popleft()
        for next in graph[cur]:
            if not dist[next]:
                dist[next] = True
                total += (d + 1) * 2
                q.append((d + 1, next))
    return total

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
answer = [float("inf"), (-1, -1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for combi in combinations(range(1, N+1), 2):
    total = bfs(combi)
    if total < answer[0]:
        answer = [total, combi]
print(answer[1][0], answer[1][1], answer[0])