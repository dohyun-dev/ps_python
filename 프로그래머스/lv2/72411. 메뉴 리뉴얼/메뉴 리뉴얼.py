from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for c in course:
        counter = defaultdict(list)
        for num, order in enumerate(orders, 1):        
            for combi in combinations(order, c):
                counter["".join(sorted(combi))].append(num)
        if counter:
            max_value = max(len(v) for v in counter.values())
            if not max_value or max_value != 1:
                for k, v in counter.items():
                    if len(v) == max_value:
                        answer.append(k)
    return sorted(answer)