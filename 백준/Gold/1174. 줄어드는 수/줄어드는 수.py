def dfs(result):
    global cnt, flag
    if result:
        answer.append(int("".join(map(lambda x: str(x), result))))
    for i in range(10):
        if not result or result[-1] > i:
            result.append(i)
            dfs(result)
            result.pop()

N = int(input())
answer = []
dfs([])
answer.sort()
print(answer[N-1] if N-1 < len(answer) else -1)