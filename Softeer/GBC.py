N, M = map(int, input().split())
limit = [[0] + list(map(int, input().split())) for _ in range(N)]
test = [[0] + list(map(int, input().split())) for _ in range(M)]
limit_arr, test_arr = [0] * 101, [0] * 101
answer = 0

for i in range(1, N):
    limit[i][0] += limit[i-1][1] + 1
    limit[i][1] += limit[i-1][1]

for i in range(1, M):
    test[i][0] += test[i-1][1] + 1
    test[i][1] += test[i-1][1]

for i in range(N):
    pre_limit_dist, limit_dist, limit_speed = limit[i]
    for j in range(pre_limit_dist, limit_dist+1):
        limit_arr[j] = limit_speed

for i in range(M):
    pre, dist, speed = test[i]
    for j in range(pre, dist+1):
        test_arr[j] = speed

print(max(0, max(test_arr[i] - limit_arr[i] for i in range(101))))