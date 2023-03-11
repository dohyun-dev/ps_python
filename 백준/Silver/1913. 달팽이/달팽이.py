N, data = int(input()), int(input())
board = [["0"] * N for _ in range(N)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d = 0
x, y, cnt = 0, 0, N ** 2 - 1
board[x][y] = str(N ** 2)
answer = (0, 0)

while True:
    for i in range(4):
        d = (d + i) % 4
        nx, ny = x + dir[d][0], y + dir[d][1]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == "0":
            board[nx][ny] = str(cnt)
            if cnt == data:
                answer = (nx, ny)
            x, y = nx, ny
            cnt -= 1
            break
    else:
        break
print("\n".join(" ".join(b) for b in board))
print(answer[0]+1, answer[1]+1)