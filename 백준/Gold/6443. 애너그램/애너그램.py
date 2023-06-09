def dfs(l=0, result=''):
    if l == len(word):
        answer.append(result)
        return

    for i in range(len(word)):
        make_word = result + word[i]

        if check[i] or make_word in check_word:
            continue

        check_word.add(make_word)
        check[i] = True
        dfs(l + 1, make_word)
        check[i] = False

answer = []
for _ in range(int(input())):
    word = sorted(input())
    check_word = set()
    check = [False] * len(word)
    dfs()
print(*answer, sep="\n")