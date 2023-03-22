import sys; sys.setrecursionlimit(10 ** 5)

def dfs1(node):
    global answer
    answer += 1
    for next in graph[node]:
        if next == -1:
            continue
        dfs1(next)
        answer += 1

def dfs2(node):
    global answer
    answer -= 1
    right = graph[node][1]
    if right != -1:
        dfs2(right)

N = int(input())
graph = {i: [-1, -1] for i in range(1, N+1)}
answer = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    graph[a] = [b, c]
dfs1(1)
dfs2(1)
print(answer)