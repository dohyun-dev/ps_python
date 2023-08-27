from collections import Counter

def solution(id_list, report, k):
    count = [[] for _ in range(len(id_list))]
    check = set()
    
    for data in report:
        if data in check:
            continue
        check.add(data)
        user1, user2 = data.split()
        count[id_list.index(user2)].append(id_list.index(user1))
    
    answer = [0] * len(id_list)
    
    for i in range(len(id_list)):
        if len(count[i]) < k:
            continue
        for j in range(len(count[i])):
            answer[count[i][j]] += 1
    return answer   