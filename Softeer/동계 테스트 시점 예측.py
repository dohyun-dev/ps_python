from collections import deque

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
level = 0

while True:
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    flag = True

    while q:
        x, y = q.popleft()
        for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if board[nx][ny] == "0":
                        q.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    if board[nx][ny] == "1" and visited[nx][ny]:
                        board[nx][ny] = "0"
                        flag = False

    if flag:
        break
    level += 1

print(level)