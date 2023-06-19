from collections import deque

def check(color1, color2):
    return 2 == color2 if color1 == 1 else 1 == color2

def bfs(green, red):
    q = deque(red + green)
    visited = [[(-1, -1)] * M for _ in range(N)]
    answer = []

    for x, y, color, level in q:
        visited[x][y] = (level, color)

    while q:
        x, y, color, level = q.popleft()

        if visited[x][y][1] == 3:
            continue

        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 0:
                if visited[nx][ny][0] == -1:
                    visited[nx][ny] = (level + 1, color)
                    q.append((nx, ny, color, level + 1))
                else:
                    if visited[nx][ny][0] == level + 1 and check(color, visited[nx][ny][1]):
                        visited[nx][ny] = (level + 1, 3)
                        answer.append((nx, ny))
    return len(answer)

def dfs(l=0, idx=0, g=[], r=[]):
    global answer
    if l == G + R:
        if len(g) == G or len(r) == R:
            answer = max(answer, bfs(g, r))
        return

    for i in range(idx, len(is_available)):
        x, y = is_available[i]
        if len(g) < G:
            g.append((x, y, 1, 0))
            dfs(l+1, i+1, g, r)
            g.pop()
        if len(r) < R:
            r.append((x, y, 2, 0))
            dfs(l+1, i+1, g, r)
            r.pop()

N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
is_available = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]
answer = 0
dfs()
print(answer)