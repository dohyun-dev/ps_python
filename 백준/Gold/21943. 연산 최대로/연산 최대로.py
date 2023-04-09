from functools import reduce

def dfs(l=0):
    global answer
    if l == N:
        answer = max(answer, reduce(lambda acc, cur: acc * cur, partitions, 1))
        return

    for i in range(Q+1):
        partitions[i] += nums[l]
        dfs(l+1)
        partitions[i] -= nums[l]

N = int(input())
nums = list(map(int, input().split()))
P, Q = map(int, input().split())
partitions = [0] * (Q+1)
answer = 0
dfs()
print(answer)