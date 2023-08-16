dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move_fire(r, c, m, s, d):
    nr = (r + dx[d] * s) % N
    nc = (c + dy[d] * s) % N

    return nr, nc, m, s, d

def move():
    new = []
    for i in range(N):
        for j in range(N):
            while board[i][j]:
                new.append(move_fire(*board[i][j].pop()))
    while new:
        r, c, m, s, d = new.pop()
        board[r][c].append((r, c, m, s, d))


def merge():
    for i in range(N):
        for j in range(N):

            if len(board[i][j]) < 2:
                continue

            new_m, new_s, odd, even = 0, 0, 0, 0
            for r, c, m, s, d in board[i][j]:
                new_m += m
                new_s += s

                if d % 2:
                    odd += 1
                else:
                    even += 1

            new_m //= 5
            new_s //= len(board[i][j])

            if new_m == 0:
                board[i][j] = []
                continue

            if not odd or not even:
                board[i][j] = [(i, j, new_m, new_s, d) for d in (0, 2, 4, 6)]
            else:
                board[i][j] = [(i, j, new_m, new_s, d) for d in (1, 3, 5, 7)]


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
answer = 0

for _ in range(M):
    # x, y, 질량, 속도, 방향
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append((r-1, c-1, m, s, d))

for _ in range(K):
    move()
    merge()

for i in range(N):
    for j in range(N):
        while board[i][j]:
            r, c, m, s, d = board[i][j].pop()
            answer += m
print(answer)