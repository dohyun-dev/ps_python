answer_gap, answer = 0, [-1]
N = 0

def calc(total, info):
    global answer_gap, answer

    apeach, lion = 0, 0
    for i in range(11):
        if total[i] == 0 and info[i] == 0:
            continue
        if total[i] > info[i]:
            lion += 10 - i
        else:
            apeach += 10 - i

    gap = abs(apeach - lion)

    if lion > apeach and gap > answer_gap:
        answer_gap = gap
        answer = list(total)

def dfs(info, l=0, idx=10, total=[0] * 11):
    if l == N:
        calc(total, info)
        return
    for i in range(idx, -1, -1):
        total[i] += 1
        dfs(info, l + 1, i, total)
        total[i] -= 1

def solution(n, info):
    global N
    N = n
    dfs(info)
    return answer