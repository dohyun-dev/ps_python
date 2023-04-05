def dfs(x, y, h, d, cnt=0):
    global answer

    if abs(ex - x) + abs(ey - y) <= h + d:
        answer = min(answer, cnt + abs(ex - x) + abs(ey - y))
        return

    for i in range(len(umb_list)):
        nx, ny = umb_list[i]
        dist = abs(x - nx) + abs(y - ny)

        if visited[i] or h + d < dist:
            continue

        visited[i] = 1
        if d >= dist:
            dfs(nx, ny, h, D, cnt+dist)
        else:
            dfs(nx, ny, h+d-dist, D, cnt+dist)
        visited[i] = 0

N, H, D = map(int, input().split())
board = [list(input()) for _ in range(N)]
sx, sy, ex, ey = -1, -1, -1, -1
umb_list = []
visited = []
answer = float('inf')
for i in range(N):
    for j in range(N):
        if board[i][j] == "S":
            sx, sy = i, j
        elif board[i][j] == "E":
            ex, ey = i, j
        elif board[i][j] == "U":
            umb_list.append((i, j))
            visited.append(0)
dfs(sx, sy, H, 0)
print(answer if answer != float("inf") else -1)