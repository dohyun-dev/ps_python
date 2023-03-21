data = input()
check = [False] * len(data)
answer = []

for i in range(len(data)):
    tmp = []
    for j in range(len(data)):
        if not check[j]:
            check[j] = True
            tmp.append(("".join(data[j] for j in range(len(data)) if check[j]), j))
            check[j] = False
    c, j = sorted(tmp)[0]
    check[j] = True
    answer.append("".join(data[j] for j in range(len(data)) if check[j]))
print(*answer, sep="\n")