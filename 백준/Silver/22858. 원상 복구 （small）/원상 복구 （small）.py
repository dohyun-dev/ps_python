N, K = map(int, input().split())
result = input().split()
cards = list(map(int, input().split()))
for _ in range(K):
    tmp = [0] * N
    for i in range(N):
        tmp[cards[i]-1] = result[i]
    result = tmp
print(" ".join(result))