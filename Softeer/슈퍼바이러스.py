def pow(num, n):
    if n == 1:
        return num

    a = pow(num, n // 2)
    return (a * a * num if n % 2 else a * a) % 1000000007

K, P, N = map(int, input().split())
print(K * pow(P, N * 10) % 1000000007)