N, M, R = map(int, input().split())
board = [input().split() for _ in range(N)]
limit = min(N // 2 , M // 2)
for _ in range(R):
    for cnt in range(limit):
        x, X, y, Y = cnt, N - cnt, cnt, M - cnt
        tmp = board[x][y]
        for i in range(y, Y-1):
            board[x][i] = board[x][i+1]
        for i in range(x, X-1):
            board[i][Y-1] = board[i+1][Y-1]
        for i in range(Y-1, y, -1):
            board[X-1][i] = board[X-1][i-1]
        for i in range(X-1, x, -1):
            board[i][y] = board[i-1][y]
        board[i][y] = tmp
print("\n".join(" ".join(b) for b in board))