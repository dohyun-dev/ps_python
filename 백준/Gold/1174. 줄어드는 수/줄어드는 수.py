def dfs(result=""):

    if result != "":
        answer.append(int(result))

    if len(answer) == 10 ** 6:
        return

    for i in range(int(result[-1]) - 1 if result else 9, -1, -1):
        dfs(result + str(i))

N = int(input())
answer = []
dfs()
answer.sort(key=lambda x: int(x))
print(answer[N - 1] if len(answer) >= N else -1)