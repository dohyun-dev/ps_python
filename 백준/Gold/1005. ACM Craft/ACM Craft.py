from collections import deque

answer = []
for t in range(int(input())):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = {i: [] for i in range(1, N + 1)}
    in_degree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for i in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    q = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            dp[i] = times[i]
            q.append(i)

    while q:
        cur = q.popleft()

        for next_node in graph[cur]:
            in_degree[next_node] -= 1
            dp[next_node] = max(dp[cur] + times[next_node], dp[next_node])
            if in_degree[next_node] == 0:
                q.append(next_node)
    answer.append(dp[int(input())])
print(*answer, sep="\n")