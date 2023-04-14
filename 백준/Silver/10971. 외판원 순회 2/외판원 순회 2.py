def dfs(start, cur, total=0, cnt=0):
    global answer
    if (cnt != 0 and cnt != N and cur == start) or answer <= total:
        return
    if cnt == N:
        if cur == start:
            answer = min(answer, total)
        return
    for i in range(N):
        if not board[cur][i] or check[i]:
            continue
        check[i] = True
        dfs(start, i, total+board[cur][i], cnt+1)
        check[i] = False

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [False] * N
answer = float("inf")
for i in range(N):
    dfs(i, i)
print(answer)