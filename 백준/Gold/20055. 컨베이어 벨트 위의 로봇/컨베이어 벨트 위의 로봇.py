from collections import deque

def turn():
    rail.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

def move():
    for i in range(N-2, -1, -1):
        if rail[i+1] == 0 or robot[i] == 0 or robot[i+1] == 1:
            continue
        rail[i+1] -= 1
        robot[i], robot[i+1] = 0, 1
    robot[-1] = 0

def raise_robot():
    if rail[0] == 0 or robot[0] == 1:
        return
    rail[0] -= 1
    robot[0] = 1

def check():
    return rail.count(0) >= K

N, K = map(int, input().split())
rail = deque(map(int, input().split()))
robot = deque([0] * N)
answer = 0

while True:
    answer += 1
    turn()
    move()
    raise_robot()
    if check():
        break
print(answer)