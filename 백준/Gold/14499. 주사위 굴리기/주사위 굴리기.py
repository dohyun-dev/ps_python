# 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def is_inner(d):
    nx, ny = dx[d] + x, dy[d] + y
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return False
    return True

def move(d):
    global x, y
    x, y = dx[d] + x, dy[d] + y

def change_dice(d):
    # 동
    if d == 1:
        dice[4], dice[1], dice[3], dice[6] = dice[6], dice[4], dice[1], dice[3]
    # 서
    elif d == 2:
        dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
    # 북
    elif d == 3:
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
    # 남
    else:
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]

def copy_value():
    if board[x][y] == 0:
        board[x][y] = dice[6]
    else:
        dice[6] = board[x][y]
        board[x][y] = 0

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [0] * 7

for order in map(int, input().split()):
    if not is_inner(order):
        continue
    move(order)
    change_dice(order)
    copy_value()
    print(dice[1])