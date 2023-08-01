import heapq

N, M, K = map(int, input().split())
graph = [[] for i in range(N + 1)]
q = []
visited = [False] * (N + 1)
answer = 0

for node in map(int, input().split()):
    heapq.heappush(q, (0, node))

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

while q:
    cost, cur = heapq.heappop(q)

    if visited[cur]:
        continue
    visited[cur] = True
    answer += cost

    for next_cost, next_node in graph[cur]:
        heapq.heappush(q, (next_cost, next_node))

print(answer)