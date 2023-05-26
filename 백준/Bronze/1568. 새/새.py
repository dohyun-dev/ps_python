import sys;input = sys.stdin.readline

n = int(input())
i = 1
result = 0

while n > 0:
    if n < i:
        i = 1
        continue
    n -= i
    result += 1
    i += 1

print(result)  