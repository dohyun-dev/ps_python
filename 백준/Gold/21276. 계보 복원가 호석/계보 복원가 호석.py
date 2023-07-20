from collections import Counter, deque

N = int(input())
names = input().split()
M = int(input())
in_degree = Counter()
graph = {name: [] for name in names}
answer = {name: [] for name in names}

for name in names:
    in_degree[name] = 0

for _ in range(M):
    a, b = input().split()
    graph[b].append(a)
    in_degree[a] += 1

q = deque([name for name in names if in_degree[name] == 0])
parent = [*q]

while q:
    cur = q.popleft()

    for next in graph[cur]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            answer[cur].append(next)
            q.append(next)

print(len(parent))
print(*parent)
for key in sorted(answer.keys()):
    print(key, end=" ")
    print(len(answer[key]), end=" ")
    print(*sorted(answer[key]))