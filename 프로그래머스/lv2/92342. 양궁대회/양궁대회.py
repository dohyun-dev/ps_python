from itertools import combinations_with_replacement

def convert(ryan_info):
    shot_result = [0] * 11
    for r in ryan_info:
        shot_result[10 - r] += 1
    return shot_result

def calc(apeach, ryan):
    apeach_score, ryan_score = 0, 0
    for i in range(11):
        if apeach[i] >= ryan[i]:
            if apeach[i] != 0:
                apeach_score += 10 - i
        else:
            ryan_score += 10 - i
    return ryan_score - apeach_score if ryan_score > apeach_score else -1

def solution(n, info):
    max_gap, answer = 0, [-1]
    for combi in map(convert, combinations_with_replacement(range(0, 11), n)):
        result = calc(info, combi)
        if max_gap < result:
            calc(info, combi)
            max_gap, answer = result, list(combi)
    return answer