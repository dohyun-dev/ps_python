def dfs(l, total, plus_cnt=0, minus_cnt=0, mul_cnt=0, div_cnt=0):
    global max_answer, min_answer
    if l == N:
        max_answer = max(max_answer, total)
        min_answer = min(min_answer, total)
        return

    if plus_cnt < plus:
        dfs(l + 1, total + nums[l], plus_cnt + 1, minus_cnt, mul_cnt, div_cnt)
    if minus_cnt < minus:
        dfs(l + 1, total - nums[l], plus_cnt, minus_cnt + 1, mul_cnt, div_cnt)
    if mul_cnt < mul:
        dfs(l + 1, total * nums[l], plus_cnt, minus_cnt, mul_cnt + 1, div_cnt)
    if div_cnt < div:
        dfs(l + 1, int(total / nums[l]), plus_cnt, minus_cnt, mul_cnt, div_cnt + 1)

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_answer = -10e9
min_answer = 10e9
dfs(1, nums[0])
print(max_answer, min_answer, sep="\n")