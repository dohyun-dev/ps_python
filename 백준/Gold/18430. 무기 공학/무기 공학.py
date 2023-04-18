dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(cnt=0, total=0):
    global answer
    x, y = cnt // M, cnt % M
    if x == N:
        answer = max(answer, total)
        return
    else:
        if not check[x][y]:
            for i in range(4):
                nx1, ny1, nx2, ny2 = dir[i][0] + x, dir[i][1] + y, dir[(i + 1) % 4][0] + x, dir[(i + 1) % 4][1] + y
                if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M and not check[nx1][ny1] and not check[nx2][ny2]:
                    tmp = board[x][y] * 2 + board[nx1][ny1] + board[nx2][ny2]
                    check[x][y] = check[nx1][ny1] = check[nx2][ny2] = True
                    dfs(cnt + 1, total + tmp)
                    check[nx1][ny1] = check[nx2][ny2] = check[x][y] = False
        dfs(cnt + 1, total)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]
answer = 0
dfs()
print(answer)