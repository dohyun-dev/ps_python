from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    total1, total2 = sum(q1), sum(q2)
    
    for i in range(min((len(q1) + len(q2)) * 2, 10 ** 8)):
        if total1 == total2:
            return i
        else:
            if total1 > total2 and q1:
                total1, total2 = total1 - q1[0], total2 + q1[0]
                q2.append(q1.popleft())
            elif total1 < total2 and q2:
                total1, total2 = total1 + q2[0], total2 - q2[0]
                q1.append(q2.popleft())
            else:
                break
    return -1