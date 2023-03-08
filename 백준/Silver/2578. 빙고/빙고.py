def search(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = "0"
                break
        else:
            continue
        break

def check():
    answer = 0
    for i in range(5):
        row_cnt, col_cnt = 0, 0
        for j in range(5):
            if board[i][j] == "0":
                row_cnt += 1
            if board[j][i] == "0":
                col_cnt += 1
        answer += 1 if row_cnt == 5 else 0
        answer += 1 if col_cnt == 5 else 0

    cnt1, cnt2 = 0, 0
    for i in range(5):
        if board[i][i] == "0":
            cnt1 += 1
        if board[i][5-i-1] == "0":
            cnt2 += 1
    answer += 1 if cnt1 == 5 else 0
    answer += 1 if cnt2 == 5 else 0
    return True if answer >= 3 else False



board = [input().split() for _ in range(5)]
answer = [input().split() for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        search(answer[i][j])
        if check():
            break
    else:
        continue
    break
print(cnt)