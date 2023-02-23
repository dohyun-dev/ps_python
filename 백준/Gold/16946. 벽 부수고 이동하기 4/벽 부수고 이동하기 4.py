from collections import deque

def bfs(x, y, group_num):
    q = deque([(x, y)])
    cnt = 1
    visited[x][y] = group_num

    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == board[x][y] and not visited[nx][ny]:
                visited[nx][ny] = group_num
                cnt += 1
                q.append((nx, ny))
    return cnt

def calc(x, y):
    total = set()
    for nx, ny in [(x, y), (x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M:
            total.add(visited[nx][ny])
    return sum(group_cnt[t] for t in total) % 10

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
group_cnt = [0]

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        if board[i][j] == 1:
            bfs(i, j, len(group_cnt))
            group_cnt.append(1)
        else:
            group_cnt.append(bfs(i, j, len(group_cnt)))

print("\n".join("".join(str(calc(i, j)) if board[i][j] == 1 else "0" for j in range(M)) for i in range(N)))