import sys; input = sys.stdin.readline;from collections import deque, defaultdict

count = 0

def BFS(x, y):
    global count
    q = deque([(x, y)])
    color = graph[x][y]

    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            count += 1
            visited[x][y] = True
            for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                tx, ty = x + dx, y + dy
                if tx >= 0 and tx < M and ty >= 0 and ty < N and graph[tx][ty] == color:
                    q.append((tx, ty))
    return count

N, M = map(int, input().rstrip().split())
graph = [input().rstrip() for _ in range(M)]
visited = [[False] * N for _ in range(M)]
counter = defaultdict(int)

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            temp = BFS(i, j)
            counter[graph[i][j]] += temp ** 2
            count = 0
print(counter['W'], counter['B'], sep='\n')