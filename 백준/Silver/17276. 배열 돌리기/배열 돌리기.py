def calc(board, o, N):
    cnt = o // 45 if o >= 0 else 8 + o // 45
    for _ in range(cnt):
        tmp = [board[N//2][i] for i in range(N)]
        for i in range(N):
            board[N//2][i] = board[N-i-1][i]
        for i in range(N):
            board[N-i-1][i] = board[N-i-1][N//2]
        for i in range(N):
            board[i][N//2] = board[i][i]
        for i in range(N):
            board[i][i] = tmp[i]

for _ in range(int(input())):
    N, O = map(int, input().split())
    board = [input().split() for _ in range(N)]
    calc(board, O, N)
    print("\n".join(" ".join(b) for b in board))