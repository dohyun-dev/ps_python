def dfs(l=0, total=0):
    global answer

    if l == N * M:
        answer = max(answer, total)
        return

    x, y = l // M, l % M

    dfs(l + 1, total)

    if check[x][y]:
        return

    check[x][y] = True
    for nx1, ny1, nx2, ny2 in [(x-1, y, x, y+1), (x, y+1, x+1, y), (x+1, y, x, y-1), (x, y-1, x-1, y)]:
        if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:

            if check[nx1][ny1] or check[nx2][ny2]:
                continue

            check[nx1][ny1], check[nx2][ny2] = True, True
            dfs(l+1, total + (board[x][y] * 2 + board[nx1][ny1] + board[nx2][ny2]))
            check[nx1][ny1], check[nx2][ny2] = False, False
    check[x][y] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]
answer = 0
dfs()
print(answer)