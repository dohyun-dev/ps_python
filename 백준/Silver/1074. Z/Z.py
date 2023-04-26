def Z(n, x, y):
    global answer
    if n == 1:
        if x == R and y == C:
            print(answer)
            exit()
        answer += 1
        return

    size = n // 2
    for i in range(x, x+size+1, size):
        for j in range(y, y+size+1, size):
            if i <= R < i + size and j <= C < j + size:
                Z(size, i, j)
            else:
                answer += size ** 2

N, R, C = map(int, input().split())
answer = 0
Z(2**N, 0, 0)