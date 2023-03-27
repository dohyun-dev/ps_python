N, M = map(int, input().split())
ice_cream = [[True] * (N+1) for _ in range(N+1)]
answer = 0

for i in range(M):
    a, b = map(int, input().split())
    ice_cream[a][b], ice_cream[b][a] = False, False

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if not ice_cream[i][j]:
            continue
        for k in range(j+1, N+1):
            if not ice_cream[i][k] or not ice_cream[j][k]:
                continue
            answer += 1
print(answer)