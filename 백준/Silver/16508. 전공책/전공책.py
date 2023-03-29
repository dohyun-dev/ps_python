from collections import Counter

def calc_price(result):
    counter = Counter([c for i in result for c in books[i][1]])
    total = sum(books[i][0] for i in result)
    for t in T:
        if t in counter:
            counter[t] -= 1
            if counter[t] == 0:
                counter.pop(t)
        else:
            break
    else:
        return total
    return 0

def dfs(l=0, result=[]):
    global answer
    if l == N:
        total = calc_price(result)
        if total != 0:
            answer = min(answer, total)
        return
    dfs(l+1, result+[l])
    dfs(l+1, result)

T, N = input(), int(input())
books = [*map(lambda x: (int(x[0]), x[1]), [input().split() for _ in range(N)])]
answer = float("inf")
dfs()
print(-1 if answer == float("inf") else answer)