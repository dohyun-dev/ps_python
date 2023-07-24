from collections import deque

N, M = int(input()), int(input())
graph = {i: [] for i in range(1, N + 1)}
in_degree = [0] * (N + 1)
dp = [[0] * (N + 1) for _ in range(N + 1)]
answer = [0] * (N + 1)

for _ in range(M):
    x, y, k = map(int, input().split())
    in_degree[x] += 1
    graph[y].append((x, k))

q = deque(i for i in range(1, N + 1) if in_degree[i] == 0)
while q:
    cur = q.popleft()

    for next_node, cost in graph[cur]:
        # 기본 부품
        if dp[cur].count(0) == N + 1:
            dp[next_node][cur] += cost
        # 중간 부품
        else:
            for i in range(1, N + 1):
                dp[next_node][i] += dp[cur][i] * cost

        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)

for i in range(1, N + 1):
    if dp[N][i] == 0:
        continue
    print(i, dp[N][i])