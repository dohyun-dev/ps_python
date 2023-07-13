from collections import deque

def bfs(start, target):
    q = deque([(start, 0, -1)])

    while q:
        cur, dist, parent = q.popleft()

        if cur == target:
            return dist

        for next, cost in tree[cur]:
            if next == parent:
                continue
            q.append((next, dist + cost, cur))
    return -1

N, M = map(int, input().split())
tree = {i: [] for i in range(1, N+1)}

for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

for query in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))