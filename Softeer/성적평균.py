N, K = map(int, input().split())
scores = [0] + list(map(int, input().split()))

for _ in range(K):
    a, b = map(int, input().split())
    print('{:.2f}'.format(sum(scores[a:b+1]) / (b-a+1)))