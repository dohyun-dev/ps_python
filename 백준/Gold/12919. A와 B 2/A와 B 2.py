def dfs(t):
    if len(t) == 0:
        return
    if t == S:
        print(1)
        exit()
    if t[0] == "B":
        dfs((t[::-1])[:-1])
    if t[-1] == "A":
        dfs(t[:-1])
S, T = input(), input()
dfs(T)
print(0)