N, X = map(int, input().split())
visitor = list(map(int, input().split()))
cnt, right = 0, 0
max_cnt, max_period = 0, 0
for left in range(N-X+1):
    while right - left != X:
        cnt += visitor[right]
        right += 1
    if cnt > max_cnt:
        max_cnt, max_period = cnt, 1
    elif cnt == max_cnt:
        max_period += 1
    cnt -= visitor[left]
if max_cnt:
    print(max_cnt, max_period, sep="\n")
else:
    print("SAD")