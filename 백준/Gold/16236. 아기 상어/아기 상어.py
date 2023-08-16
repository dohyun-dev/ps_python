from collections import deque
from heapq import heappush, heappop

def search_fish():
    q = deque([(shark[1], shark[2])])
    visited = [[False] * N for _ in range(N)]
    visited[shark[1]][shark[2]] = True
    fishes = []
    level = 0

    while q:
        level += 1
        for _ in range(len(q)):
            x, y = q.popleft()

            for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if board[nx][ny] in (0, 9):
                        q.append((nx, ny))
                    else:
                        if board[nx][ny] > shark[0]:
                            continue
                        if board[nx][ny] < shark[0]:
                            heappush(fishes, (level, nx, ny))
                        q.append((nx, ny))
        if fishes:
            break
    return heappop(fishes) if fishes else (-1, -1, -1)

def eat_fish(distance, x, y):
    global answer
    answer += distance

    board[shark[1]][shark[2]], board[x][y] = 0, 9
    shark[1], shark[2] = x, y
    shark[3] += 1

    if shark[0] == shark[3]:
        shark[0] += 1
        shark[3] = 0

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark = [2, 0, 0, 0] # 크기, x 좌표, y좌표, 먹은 물고기 수
answer = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark[1], shark[2] = i, j
            break
    else:
        continue
    break

while True:
    distance, x, y = search_fish()
    if distance == -1:
        break
    eat_fish(distance, x, y)
print(answer)