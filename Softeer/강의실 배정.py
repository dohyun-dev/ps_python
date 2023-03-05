import sys; input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
q = []

for _ in range(N):
    s, e = map(int, input().split())
    heappush(q, (e, s))

end_time, answer = 0, 0
while q:
    end, start = heappop(q)
    if start >= end_time:
        answer += 1
        end_time = end
print(answer)