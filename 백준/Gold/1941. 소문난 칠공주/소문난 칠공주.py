from collections import deque

def bfs(result):
    q = deque([result[0]])
    x, y = result[0]
    visited = 0 | 1 << (x * N + y)
    total = 1

    while q:
        x, y = q.popleft()

        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and not visited & 1 << (nx * N + ny) and (nx, ny) in result:
                visited |= 1 << (nx * N + ny)
                total += 1
                q.append((nx, ny))
    return total == 7

def dfs(l=0, idx=0, y_count=0, result=[]):
    global answer

    if y_count == 4:
        return

    if l == 7:
        if bfs(result):
            answer += 1
        return

    for i in range(idx, N ** 2):
        x, y = i // N, i % N
        dfs(l+1, i+1, y_count + (board[x][y] == "Y"), result + [(x, y)])

N = 5
board = [list(input()) for _ in range(N)]
answer = 0
dfs()
print(answer)