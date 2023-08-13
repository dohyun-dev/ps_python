watches = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def watch():
    for cctv_num in range(len(cctv)):
        cctv_type, x, y = cctv[cctv_num]
        for d in watches[cctv_type][permu[cctv_num]]:
            nx = x + dx[d]
            ny = y + dy[d]
            while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
                if board[nx][ny] == 0:
                    board[nx][ny] = 7
                nx = nx + dx[d]
                ny = ny + dy[d]

def clean_watch():
    for cctv_num in range(len(cctv)):
        cctv_type, x, y = cctv[cctv_num]
        for d in watches[cctv_type][permu[cctv_num]]:
            nx = x + dx[d]
            ny = y + dy[d]
            while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
                if board[nx][ny] == 7:
                    board[nx][ny] = 0
                nx = nx + dx[d]
                ny = ny + dy[d]

def dfs(l=0):
    global answer
    if l == len(cctv):
        watch()
        answer = min(answer, len([1 for i in range(N) for j in range(M) if not board[i][j]]))
        clean_watch()
        return
    for i in range(len(watches[cctv[l][0]])):
        permu[l] = i
        dfs(l+1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv = [(board[i][j], i, j) for i in range(N) for j in range(M) if board[i][j] not in (0, 6)]
permu = [0] * len(cctv)
answer = float("inf")
dfs()
print(answer)