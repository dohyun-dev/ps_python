def solution(id_list, report, k):
    count = [[] for _ in range(len(id_list))]
    answer = [0] * len(id_list)
    
    for data in set(report):
        user1, user2 = data.split()
        count[id_list.index(user2)].append(id_list.index(user1))
    
    for i in range(len(id_list)):
        if len(count[i]) < k:
            continue
        for j in range(len(count[i])):
            answer[count[i][j]] += 1
    return answer   