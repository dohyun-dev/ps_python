N, M = map(int, input().split())
arr1, arr2 = [list(map(int, input().split())) for _ in range(N)], [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr1[i][j] += arr2[i][j]
for i in range(N):
    print(" ".join(map(lambda x: str(x), arr1[i])))