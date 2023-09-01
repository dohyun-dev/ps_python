import re
from itertools import permutations

def calc(a, o, b):
    if o == "+":
        return str(int(a) + int(b))
    elif o == "-":
        return str(int(a) - int(b))
    else:
        return str(int(a) * int(b))

def solution(expression):
    answer = 0
    for p in permutations("+-*"):
        tmp = re.findall("\w+|[+*-]", expression)
        for oper in p:
            while oper in tmp:
                oper_idx = tmp.index(oper)
                tmp = tmp[:oper_idx-1] + [calc(*tmp[oper_idx-1:oper_idx+2])] + tmp[oper_idx+2:]
        answer = max(answer, abs(int(tmp[0])))
    return answer