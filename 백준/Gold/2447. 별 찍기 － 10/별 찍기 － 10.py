def star(n, x, y):
    if n == 1:
        board[x][y] = "*"
        return
    size, cnt = n // 3, 0
    for i in range(x, x + n, size):
        for j in range(y, y + n, size):
            cnt += 1
            if cnt == 5:
                continue
            star(size, i, j)

N = int(input())
board = [[" "] * N for _ in range(N)]
star(N, 0, 0)
print("\n".join("".join(b) for b in board))