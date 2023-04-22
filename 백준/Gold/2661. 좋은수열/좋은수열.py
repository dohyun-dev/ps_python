def check(tmp):
    if len(tmp) == 1:
        return True
    for limit in range(1, len(tmp) // 2 + 1):
        for i in range(0, len(tmp) - limit * 2 + 1):
            if tmp[i:i+limit] == tmp[i+limit:i+limit*2]:
                return False
    return True


def dfs(result=""):
    if len(result) == N:
        print(result)
        exit()

    for i in ("1", "2", "3"):
        tmp = result + i
        if check(tmp):
            dfs(tmp)

N = int(input())
answer = []
dfs()