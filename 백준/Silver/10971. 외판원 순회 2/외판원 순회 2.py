def dfs(l, cur, start, total=0):
    global answer
    if total >= answer:
        return
    if l == N:
        if cur == start:
            answer = total + board[cur][start]
    for i in range(N):
        if check[i] or not board[cur][i]:
            continue
        check[i] = True
        dfs(l+1, i, start, total + board[cur][i])
        check[i] = False

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [False] * N
answer = float("inf")
for i in range(N):
    dfs(0, i, i)
print(answer)