def search(index):
    for i in range(K, 0, -1):
        minus_i = max(index-i, 0)
        if data[minus_i] == "H" and not check[minus_i]:
            check[minus_i] = 1
            return True
    for i in range(1, K+1):
        plus_i = min(i+index, N-1)
        if data[plus_i] == "H" and not check[plus_i]:
            check[plus_i] = 1
            return True
    return False

N, K = map(int, input().split())
data = input()
check = [0] * N
answer = 0
for i, c in enumerate(data):
    if c == "P":
        if search(i):
            answer += 1
print(answer)