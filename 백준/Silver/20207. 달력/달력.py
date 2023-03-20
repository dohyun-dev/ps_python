N = int(input())
board = [0] * 366
answer = 0

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        board[i] += 1

flag, cnt, max_cnt = False, 0, 0
for i in range(366):
    if flag:
        if board[i]:
            cnt += 1
            max_cnt = max(max_cnt, board[i])
        else:
            answer += cnt * max_cnt
            flag, cnt, max_cnt = False, 0, 0
    elif board[i]:
        flag = True
        cnt, max_cnt = 1, 1
if flag:
    answer += cnt * max_cnt
print(answer)