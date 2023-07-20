from heapq import heappush, heappop, heapify

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = {i: [] for i in range(1, N + 1)}
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    in_degree[b] += 1
    graph[a].append(b)

q = [i for i in range(1, N + 1) if in_degree[i] == 0]
heapify(q)
while q:
    cur = heappop(q)
    answer.append(cur)

    for next_node in graph[cur]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            heappush(q, next_node)
print(*answer)