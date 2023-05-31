N = int(input())
board = [[0] * N for _ in range(N)]

for i in range(N):
    board[i] = [0] + (list(map(int, input().split())) + [0] * (N - i - 1))

for i in range(1,N):
    for j in range(1, i+2):
        board[i][j] = max(board[i-1][j-1], board[i-1][j]) + board[i][j]

print(max(board[-1]))