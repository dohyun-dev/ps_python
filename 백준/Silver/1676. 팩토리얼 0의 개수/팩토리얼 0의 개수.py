import sys; input = lambda : sys.stdin.readline().rstrip()
from math import factorial

n = factorial(int(input()))
count = 0

while n % 10 == 0:
    n //= 10
    count += 1

print(count)