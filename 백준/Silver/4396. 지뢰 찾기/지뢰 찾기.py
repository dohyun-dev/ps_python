N = int(input())
board = [list(input()) for _ in range(N)]
answer = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if answer[i][j] == "x" and board[i][j] == "*":
            for x in range(N):
                for y in range(N):
                    if board[x][y] == "*":
                        answer[x][y] = "*"
        if answer[i][j] == "x":
            total = 0
            for x in range(max(i-1, 0), min(i+2, N)):
                for y in range(max(j-1, 0), min(j+2, N)):
                    if board[x][y] == "*":
                        total += 1
            answer[i][j] = str(total)
print("\n".join("".join(a) for a in answer))