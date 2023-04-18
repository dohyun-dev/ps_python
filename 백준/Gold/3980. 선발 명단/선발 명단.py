def dfs(l=0, total=0):
    global answer
    if l == 11:
        answer = max(answer, total)
        return
    for i in range(11):
        if not positions[l][i] or check[i]:
            continue
        check[i] = True
        dfs(l+1, total + positions[l][i])
        check[i] = False


for t in range(int(input())):
    answer = 0
    positions = [list(map(int, input().split())) for _ in range(11)]
    check = [False] * 11
    dfs()
    print(answer)