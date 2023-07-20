from collections import deque

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
indegree = [0] * (N + 1)

for _ in range(M):
    temp = list(map(int, input().split()[1:]))
    for i in range(len(temp)-1):
        graph[temp[i]].append(temp[i+1])
        indegree[temp[i+1]] += 1


q = deque([i for i in range(1, N+1) if not indegree[i]])
answer = []
while q:
    cur = q.popleft()
    answer.append(str(cur))

    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)

print("\n".join(answer) if len(answer) == N else 0)