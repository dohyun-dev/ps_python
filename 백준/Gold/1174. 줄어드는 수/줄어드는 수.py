def dfs(result):
    if len(answer) == 1000000:
        return
    answer.append(int(result))
    for i in range(int(result[-1])):
        dfs(result + str(i))

N = int(input())
answer = []
for i in range(10):
    dfs(str(i))
answer.sort()
print(answer[N-1] if len(answer) >= N else -1)