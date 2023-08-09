dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(clouds, d, s):
    new_clouds = []
    for cx, cy in clouds:
        nx = (cx + dx[d] * s) % N
        ny = (cy + dy[d] * s) % N
        new_clouds.append((nx, ny))
    return new_clouds

def rain_drop(clouds):
    for cx, cy in clouds:
        board[cx][cy] += 1

def make_cloud(clouds):
    new_clouds = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] < 2 or (i, j) in clouds:
                continue
            new_clouds.add((i, j))
            board[i][j] -= 2
    return new_clouds

def copy_water(x, y):
    cnt = 0
    for nx, ny in [(x-1, y-1), (x-1, y+1), (x+1, y+1), (x+1, y-1)]:
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] != 0:
            cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
clouds = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}

for _ in range(M):
    d, s = map(int, input().split())
    clouds = move_cloud(clouds, d, s)
    rain_drop(clouds)

    for cx, cy in clouds:
        board[cx][cy] += copy_water(cx, cy)

    clouds = make_cloud(clouds)

print(sum(board[i][j] for i in range(N) for j in range(N)))