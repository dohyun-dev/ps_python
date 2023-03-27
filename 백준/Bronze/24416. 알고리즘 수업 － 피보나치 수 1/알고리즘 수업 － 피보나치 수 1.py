cnt1, cnt2, dp = 0, 0, [0, 1, 1]

def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cnt2
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])
        cnt2 += 1

n = int(input())
fib(n)
fibonacci(n)
print(cnt1, cnt2)