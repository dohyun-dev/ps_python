N, M, R = map(int, input().split())
board = [[float("inf")] * N for _ in range(N)]
items = list(map(int, input().split()))

for _ in range(R):
    a, b, l = map(int, input().split())
    board[a-1][b-1] = l
    board[b-1][a-1] = l


for mid in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            board[i][j] = min(board[i][j], board[i][mid] + board[mid][j])

answer = 0
for i in range(N):
    total = 0
    for j, cost in enumerate(board[i]):
        if cost > M:
            continue
        total += items[j]
    answer = max(answer, total + items[i])
print(answer)