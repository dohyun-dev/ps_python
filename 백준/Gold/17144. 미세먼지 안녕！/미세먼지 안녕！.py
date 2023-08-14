def spread_dust():
    dusts = [(i, j, board[i][j]) for i in range(R) for j in range(C) if board[i][j] > 0]

    for x, y, dust in dusts:
        cnt = 0
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] >= 0:
                board[nx][ny] += dust // 5
                cnt += 1
        board[x][y] -= dust // 5 * cnt

def clean_dust():
    # 위쪽 공기청정기 공기 가동
    tx, ty = top_air_cleaner

    for nx in range(tx-1, 0, -1):
        board[nx][0] = board[nx-1][0]

    for ny in range(0, C-1):
        board[0][ny] = board[0][ny+1]

    for nx in range(tx):
        board[nx][C-1] = board[nx+1][C-1]

    for ny in range(C-1, 1, -1):
        board[tx][ny] = board[tx][ny-1]
    board[tx][1] = 0

    # 아래쪽 공기청정기 가동
    tx, ty = down_air_cleaner

    for nx in range(tx+1, R-1):
        board[nx][0] = board[nx+1][0]

    for ny in range(C-1):
        board[R-1][ny] = board[R-1][ny+1]

    for nx in range(R-1, tx, -1):
        board[nx][C-1] = board[nx-1][C-1]

    for ny in range(C-1, 1, -1):
        board[tx][ny] = board[tx][ny-1]
    board[tx][1] = 0



R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
top_air_cleaner = None
down_air_cleaner = None

# 공기 청정기 위치 설정
for i in range(R):
    if board[i][0] == -1:
        if top_air_cleaner == None:
            top_air_cleaner = i, 0
        else:
            down_air_cleaner = i, 0

for _ in range(T):
    spread_dust()
    clean_dust()

print(sum(board[i][j] for i in range(R) for j in range(C) if board[i][j] != -1))