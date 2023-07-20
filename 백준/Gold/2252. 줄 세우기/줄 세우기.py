from collections import deque, defaultdict

N, M = map(int, input().split())
in_degree = [0 for _ in range(N + 1)]
graph = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    in_degree[b] += 1
    graph[a].append(b)

q = deque(i for i in range(1, N + 1) if not in_degree[i])
answer = []

while q:
    cur = q.popleft()
    answer.append(cur)

    for node in graph[cur]:
        in_degree[node] -= 1
        if not in_degree[node]:
            q.append(node)

print(*answer)