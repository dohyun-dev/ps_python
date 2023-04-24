def solve(n, x, y):
    if n == 1:
        return (1, 0) if board[x][y] else (0, 1)

    size, cnt1, cnt2 = n // 2, 0, 0
    tmp = []

    tmp.append(solve(size, x, y))
    tmp.append(solve(size, x, y + size))
    tmp.append(solve(size, x + size, y))
    tmp.append(solve(size, x + size, y + size))

    for b, w in tmp:
        cnt1, cnt2 = cnt1 + b, cnt2 + w

    if cnt1 == 4 and cnt2 == 0:
        return (1, 0)
    elif cnt2 == 4 and cnt1 == 0:
        return (0, 1)
    else:
        return (cnt1, cnt2)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
blue, white = solve(N, 0, 0)
print(white, blue, sep="\n")