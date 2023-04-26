def solve(x, y, n):
    if n == 1:
        return board[x][y]
    tmp = []
    for i in range(x, x + n // 2 + 1, n // 2):
        for j in range(y, y + n // 2 + 1, n // 2):
            tmp.append(solve(i, j, n // 2))
    tmp.sort()
    return tmp[-2]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solve(0, 0, N))