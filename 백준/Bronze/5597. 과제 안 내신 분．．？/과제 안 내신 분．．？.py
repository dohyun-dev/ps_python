check = [False] * 31
for _ in range(28):
    check[int(input())] = True
print("\n".join(str(i) for i in range(1, 31) if not check[i]))