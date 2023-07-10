def pre(node, result):
    if node == ".":
        return

    result.append(node)
    pre(tree[node][0], result)
    pre(tree[node][1], result)

def mid(node, result):
    if node == ".":
        return

    mid(tree[node][0], result)
    result.append(node)
    mid(tree[node][1], result)

def post(node, result):
    if node == ".":
        return

    post(tree[node][0], result)
    post(tree[node][1], result)
    result.append(node)

N = int(input())
tree = {chr(i + ord("A")): [".", "."] for i in range(N)}

for _ in range(N-1):
    p, l, r = input().split()
    tree[p] = [l, r]

result = [[] for _ in range(3)]
pre('A', result[0])
mid('A', result[1])
post('A', result[2])

print(*["".join(result[i]) for i in range(3)], sep="\n")