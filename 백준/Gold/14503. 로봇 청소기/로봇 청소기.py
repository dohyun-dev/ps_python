# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def next_check(x, y):
    if x < 0 or x >= N or y < 0 or y >= M or is_wall(x, y):
        return False
    return True

def is_clean(x, y):
    return board[x][y] == 2

def is_wall(x, y):
    return board[x][y] == 1

def around_check(x, y, d):
    for i in range(4):
        nx = x + dx[(d + i) % 4]
        ny = y + dy[(d + i) % 4]

        # 청소가 되어 있지 않다면
        if not is_wall(nx, ny) and not is_clean(nx, ny):
            return False
    return True

def move_back(x, y, d):
    nx = x + dx[(d + 2) % 4]
    ny = y + dy[(d + 2) % 4]

    return nx, ny

def turn(d):
    return 3 if d - 1 == -1 else d - 1

def move_front(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]
    return (nx, ny)


def solution(x, y, d):
    clean_count = 0

    while True:
        # 현재 칸이 청소 되어 있는지 체크
        if not is_clean(x, y):
            # 1. 청소를 진행한다.
            board[x][y] = 2
            clean_count += 1
        else:
            if around_check(x, y, d):
                # 2. 4칸이 청소가 모두 되어 있다면
                nx, ny = move_back(x, y, d)

                # 2-2 벽이거나 범위 밖이라면 로복청소기 종료
                if not next_check(nx, ny):
                    break

                # 2-1 방향을 유지한 채로 한 칸 후진
                x, y = nx, ny
            else:
                # 3. 청소가 되어 있지 않은 칸이 있다면
                for i in range(4):
                    # 3-1 반시계 방향으로 90도 회전
                    d = turn(d)

                    nx, ny = move_front(x, y, d)

                    # 범위 및 벽 체크
                    if not next_check(nx, ny):
                        continue

                    # 청소 되어 있는 칸인지 체크
                    if not is_clean(nx, ny):
                        # 3-2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                        x, y = nx, ny
                        break
                else:
                    break
    return clean_count


N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(x, y, d))