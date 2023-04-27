def quad_tree(n, x, y):
    if n == 1:
        return board[x][y]
    size, result = n // 2, ""
    for i in range(x, x + size + 1, size):
        for j in range(y, y + size + 1, size):
            if len(set(board[nx][ny] for nx in range(i, i + size) for ny in range(j, j + size))) == 1:
                result += board[i][j]
            else:
                result += f'{quad_tree(size, i, j)}'
    return result[0] if len(set(result)) == 1 else "(" + result + ")"

N = int(input())
board = [input() for _ in range(N)]
print(quad_tree(N, 0, 0))