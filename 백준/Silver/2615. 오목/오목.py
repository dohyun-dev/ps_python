dir = [(1, 0), (0, 1), (1, 1), (-1, 1)]

def check(x, y, cur):
    for i in range(4):
        nx, ny = x, y
        cnt = 0
        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == cur:
            cnt += 1

            if cnt == 5:
                if 0 <= x - dir[i][0] < 19 and 0 <= y - dir[i][1] < 19 and board[x - dir[i][0]][y - dir[i][1]] == cur:
                    break
                if 0 <= nx + dir[i][0] < 19 and 0 <= ny + dir[i][1] < 19 and board[nx + dir[i][0]][ny + dir[i][1]] == cur:
                    break
                return True
            nx, ny = nx + dir[i][0], ny + dir[i][1]
    return False

board = [input().split() for _ in range(19)]

for i in range(19):
    for j in range(19):
        if board[i][j] != "0" and check(i, j, board[i][j]):
            print(board[i][j])
            print(i+1, j+1)
            exit()
print(0)