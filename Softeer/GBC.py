N, M = map(int, input().split())
limit = [tuple(map(int, input().split())) for _ in range(N)]
real_speed = [tuple(map(int, input().split())) for _ in range(N)]
width_limit, real_limit, ptr = 0, 0, 0
answer = 0

for width, speed in real_speed:
    real_limit += width
    while real_limit > width_limit:
        answer = max(answer, speed - limit[ptr][1])
        width_limit += limit[ptr][0]
        ptr += 1
print(answer)