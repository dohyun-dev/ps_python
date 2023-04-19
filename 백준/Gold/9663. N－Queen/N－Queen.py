def dfs(x):
    global answer
    if x == N-1:
        answer += 1
        return
    for i in range(N):
        if board[i] != -1:
            continue
        flag = True
        for j in range(N):
            if board[j] != -1 and abs(x + 1 - board[j]) == abs(i - j):
                flag = False
                break
        if flag:
            board[i] = x + 1
            dfs(x+1)
            board[i] = -1

N = int(input())
board = [-1] * N
answer = 0
for i in range(N):
    board[i] = 0
    dfs(0)
    board[i] = -1
print(answer)