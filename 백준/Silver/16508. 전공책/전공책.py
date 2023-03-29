from collections import Counter

def dfs(l=0, total_price=0, word_counter=Counter()):
    global answer
    if answer < total_price:
        return
    if l == N:
        if len((t_counter - word_counter).keys()) == 0:
            answer = min(answer, total_price)
        return
    price, title = books[l]
    current_counter = Counter(title)
    dfs(l+1, total_price+price, word_counter+current_counter)
    dfs(l+1, total_price, word_counter)

T, N = input(), int(input())
books = [*map(lambda x: (int(x[0]), x[1]), [input().split() for _ in range(N)])]
t_counter = Counter(T)
answer = float("inf")
dfs()
print(-1 if answer == float("inf") else answer)