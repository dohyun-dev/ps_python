def dfs(cur, parent=-1):
    visited[cur] = True

    for next_node in graph[cur]:
        if next_node == parent:
            continue
        if visited[next_node] or not dfs(next_node, cur):
            return False
    return True

t = 1
while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    graph = {i: [] for i in range(1, N + 1)}
    visited = [False] * (N + 1)
    answer = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        if visited[i]:
            continue
        if dfs(i):
            answer += 1

    if answer > 1:
        print("Case {:d}: A forest of {:d} trees.".format(t, answer))
    elif answer == 1:
        print("Case {:d}: There is one tree.".format(t))
    else:
        print("Case {:d}: No trees.".format(t))
    t += 1