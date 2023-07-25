import heapq

def prim(start):
    q = []
    visited = [False] * N
    visited[start] = True
    answer = 0

    for i in range(N):
        if start == i:
            continue
        heapq.heappush(q, (graph[start][i], i))

    while q:
        cost, cur = heapq.heappop(q)

        if visited[cur]:
            continue

        visited[cur] = True
        answer += cost

        for i in range(N):
            if cur == i:
                continue
            heapq.heappush(q, (graph[cur][i], i))
    return answer

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
print(prim(0))