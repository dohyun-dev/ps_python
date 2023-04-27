import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque; 

N, M = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(i for i in range(1, N+1))
cnt = 0

for num in arr:
    while True:
        if q[0] == num:
            q.popleft()
            break
        else:
            t = q.index(num) 
            if t <= len(q) // 2:
                q.rotate(-t)
                cnt += t
            else:
                q.rotate(len(q) - t)
                cnt += len(q) - t

print(cnt)