def dfs(l=0, result=[]):
    if l == M:
        print(" ".join(result))
        return
    for i in range(1, N+1):
        if check[i]:
            continue
        check[i] = True
        result.append(str(i))
        dfs(l+1, result)
        result.pop()
        check[i] = False

N, M = map(int, input().split())
check = [False] * (N + 1)
dfs()