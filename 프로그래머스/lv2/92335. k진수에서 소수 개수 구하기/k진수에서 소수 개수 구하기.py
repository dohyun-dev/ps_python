import re

def convert(num, k):
    result = ""
    while num > 0:
        result = str(num % k) + result
        num //= k
    return result

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    n = convert(n, k)
    answer = 0
    for num in n.split('0'):
        if num and is_prime(int(num)):
            answer += 1
    return answer