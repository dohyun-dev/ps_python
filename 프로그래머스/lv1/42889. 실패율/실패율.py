def solution(N, stages):
    count = [0] * (N + 2)
    
    for stage in stages:
        count[stage] += 1
        
    answer = []
        
    for i in range(1, N + 1):
        a, b = count[i], sum(count[i:])
        if b == 0:
            answer.append((i, 0))
        else:
            answer.append((i, a / b))
        
    return list(map(lambda x: x[0], sorted(answer, key=lambda x: (-x[1], x[0]))))