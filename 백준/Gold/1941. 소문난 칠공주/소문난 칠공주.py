def dfs(pre, s=1, y=0):
    if s + y == 7:
        answer.add(str(sorted(pre)))
        return

    for r, c in pre:
        for nx, ny in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in pre:
                if board[nx][ny] == "S":
                    pre.add((nx, ny))
                    dfs(pre, s+1, y)
                    pre.remove((nx, ny))
                elif board[nx][ny] == "Y" and y <= 2:
                    pre.add((nx, ny))
                    dfs(pre, s, y+1)
                    pre.remove((nx, ny))

N = 5
board = [list(input()) for _ in range(N)]
answer = set()

for i in range(N):
    for j in range(N):
        if board[i][j] == "Y":
            continue
        dfs({(i, j)})
print(len(answer))