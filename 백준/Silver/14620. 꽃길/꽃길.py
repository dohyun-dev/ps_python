def check(x, y):
    return all(False for nx, ny in [(x, y), (x-1, y), (x, y+1), (x+1,y), (x, y-1)] if flag[nx][ny])
def change(x, y):
    total = 0
    for nx, ny in [(x, y), (x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        flag[nx][ny] = not flag[nx][ny]
        total += board[nx][ny]
    return total

def dfs(l, r, c, total=0):
    global answer
    if l == 3:
        answer = min(answer, total)
        return

    for i in range(r, N-1):
        c = c if r == i else 1
        for j in range(c, N-1):
            if check(i, j):
                add_price = change(i, j)
                dfs(l+1, i, j+1, total+add_price)
                change(i, j)

N = int(input())
flag = [[False] * N for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
dfs(0, 1, 1)
print(answer)