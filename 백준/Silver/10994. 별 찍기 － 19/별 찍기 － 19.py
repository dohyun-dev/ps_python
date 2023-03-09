def calc_limit(n):
    return 4 * (n-1) + 1

def solve(x, y, n):
    limit = calc_limit(n)
    if n == 1:
        board[x][y] = "*"
        return
    for i in range(x, x+limit):
        for j in range(y, y+limit):
            if i == x or i == x+limit-1:
                board[i][j] = "*"
            elif j == y or j == y+limit-1:
                board[i][j] = "*"
    solve(x+2, y+2, n-1)

N = int(input())
limit = calc_limit(N)
board = [[" "] * limit for i in range(limit)]
solve(0, 0, N)
print("\n".join("".join(b) for b in board))