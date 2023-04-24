N, X = map(int, input().split())
visitor = list(map(int, input().split()))
total = sum(visitor[:X])
max_cnt, cnt = total, 1

for i in range(X, N):
    total += visitor[i]
    total -= visitor[i-X]
    if max_cnt < total:
        max_cnt = total
        cnt = 1
    elif max_cnt == total:
        cnt += 1
if max_cnt:
    print(max_cnt, cnt, sep="\n")
else:
    print("SAD")