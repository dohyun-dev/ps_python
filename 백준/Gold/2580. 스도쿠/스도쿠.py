def make_check_set(x, y):
    check_set = set()
    for i in range(9):
        if board[x][i] != 0:
            check_set.add(board[x][i])
        if board[i][y] != 0:
            check_set.add(board[i][y])
    row_start, col_start = x // 3 * 3, y // 3 * 3
    for nx in range(row_start, row_start + 3):
        for ny in range(col_start, col_start + 3):
            if board[nx][ny] != 0:
                check_set.add(board[nx][ny])
    return set(range(1, 10)) - check_set

def dfs(l=0):
    if l == len(zero_list):
        for i in range(9):
            print(" ".join(map(str, board[i])))
        exit()
    x, y =  zero_list[l]
    for num in make_check_set(x, y):
        board[x][y] = num
        dfs(l+1)
        board[x][y] = 0

board = [list(map(int, input().split())) for _ in range(9)]
zero_list = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero_list.append((i, j))
dfs()