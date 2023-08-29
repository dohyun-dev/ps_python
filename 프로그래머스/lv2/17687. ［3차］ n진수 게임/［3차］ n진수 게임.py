def convert(num, k):
    if num == 0:
        return "0"
    answer = ""
    while num > 0:
        d, m = divmod(num, k)
        answer = "0123456789ABCDEF"[m] + answer
        num = d
    return answer

def solution(n, t, m, p):
    nums = " "
    answer = ""
    
    for i in range(m * t):
        nums += convert(i, n)
    
    while len(answer) < t:
        answer += nums[p]
        p += m
    
    return answer