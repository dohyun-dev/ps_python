def dfs(l=0, result=""):
    if l == len(word):
        if result not in check_set1:
            check_set1.add(result)
            print(result)
        return
    for i, c in enumerate(word):
        if check[i] or result + c in check_set2:
            continue
        check[i] = True
        check_set2.add(result + c)
        dfs(l+1, result + c)
        check[i] = False

check_set1 = set()
for _ in range(int(input())):
    word = sorted(input())
    check = [False] * len(word)
    check_set2 = set()
    dfs()