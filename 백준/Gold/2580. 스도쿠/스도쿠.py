def get_available_number(x, y):
    x_start, y_start = x // 3 * 3, y // 3 * 3
    exist_number = set()

    for i in range(x_start, x_start + 3):
        for j in range(y_start, y_start + 3):
            exist_number.add(board[i][j])

    for i in range(9):
        exist_number.add(board[x][i])
        exist_number.add(board[i][y])

    return set(range(1, 10)) - exist_number

def dfs(cnt=0):
    if cnt == 9 ** 2:
        for b in board:
            print(*b)
        exit()

    x, y = cnt // 9, cnt % 9

    if board[x][y] == 0:
        for num in get_available_number(x, y):
            board[x][y] = num
            dfs(cnt + 1)
            board[x][y] = 0
    else:
        dfs(cnt + 1)

board = [list(map(int, input().split())) for _ in range(9)]
dfs()