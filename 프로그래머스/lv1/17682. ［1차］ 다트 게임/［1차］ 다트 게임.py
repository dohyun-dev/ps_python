import re

def solution(dartResult):
    answer = []
    
    for dart in re.findall('[0-9]{1,2}[SDT][*#]?', dartResult):
        match = re.match("([0-9]{1,2})([SDT])([*#]?)", dart)
        
        num = int(match.group(1))
        bonus = 1 if match.group(2) == "S" else 2 if match.group(2) == "D" else 3
        opt = match.group(3)
        
        answer.append(num ** bonus)
        
        if opt == "*":
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif opt == "#":
            answer[-1] = -answer[-1]
        
    return sum(answer)