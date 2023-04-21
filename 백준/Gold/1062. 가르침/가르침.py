def dfs(l=0, idx=0):
    global answer
    if l == K:
        cnt = 0
        for word in words:
            for c in word:
                if not check[ord(c) - ord('a')]:
                    break
            else:
                cnt += 1
        answer = max(answer, cnt)
        return

    for i in range(idx, 26):
        if check[i]:
            continue
        check[i] = True
        dfs(l+1, i + 1)
        check[i] = False

N, K = map(int, input().split())
K -= 5
if K < 0:
    print(0)
else:
    check = [False] * 26
    for c in "antic":
        check[ord(c) - ord('a')] = True
    words = [input()[4:-4] for _ in range(N)]
    answer = 0
    dfs()
    print(answer)