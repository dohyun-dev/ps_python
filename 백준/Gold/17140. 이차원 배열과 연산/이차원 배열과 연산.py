from collections import Counter

def compare():
    return R if len(board) >= len(board[0]) else C

def R():
    for i, b in enumerate(board):
        counter, tmp = Counter(b), []
        for k, v in filter(lambda x: x[0] != 0, sorted(counter.most_common(), key=lambda x: (x[1], x[0]))):
            tmp += [k, v]
        board[i] = tmp[:100]
    max_col = max(len(b) for b in board)
    for i, b in enumerate(board):
        board[i] = b + [0] * (max_col - len(b))

def C():
    global board
    board = [list(b) for b in zip(*board)]
    R()
    board = [list(b) for b in zip(*board)]

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
    if r-1 < len(board) and c-1 < len(board[r-1]) and board[r-1][c-1] == k:
        print(i)
        break
    compare()()
else:
    print(-1)