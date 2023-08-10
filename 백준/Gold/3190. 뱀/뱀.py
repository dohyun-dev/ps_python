from collections import deque

def move(d):
    x, y = body[-1]
    nx, ny = x + dx[d], y + dy[d]
    return nx, ny

def turn(c):
    global d
    if c == "L":
        d = 3 if d == 0 else d - 1
    else:
        d = (d + 1) % 4

def is_game_over(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    if board[x][y] == 2:
        return True
    return False

def exist_apple(x, y):
    if board[x][y] == 1:
        return True
    return False

def delete_body(body):
    x, y = body.popleft()
    board[x][y] = 0


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [[0] * N for i in range(N)]
directions = deque()
body = deque([(0, 0)])
board[0][0] = 2
d, time = 1, 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

for _ in range(int(input())):
    x, c = tuple(input().split())
    directions.append((int(x), c))

while True:
    time += 1
    x, y = move(d)

    if is_game_over(x, y):
        break

    if not exist_apple(x, y):
        delete_body(body)
    board[x][y] = 2
    body.append((x, y))

    if directions and directions[0][0] == time:
        x, c = directions.popleft()
        turn(c)
print(time)