from collections import deque

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

q = deque([(K, 0, 0)])
dist = [[[0] * M for _ in range(N)] for _ in range(K+1)]
dist[K][0][0] = 1
while q:
    life, x, y = q.popleft()

    if x == N-1 and y == M-1:
        print(dist[life][x][y])
        exit()

    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == "1":
                if life == 0 or dist[life-1][nx][ny]:
                    continue
                dist[life-1][nx][ny] = dist[life][x][y] + 1
                q.append((life-1, nx, ny))
            else:
                if dist[life][nx][ny]:
                    continue
                dist[life][nx][ny] = dist[life][x][y] + 1
                q.append((life, nx, ny))
print(-1)