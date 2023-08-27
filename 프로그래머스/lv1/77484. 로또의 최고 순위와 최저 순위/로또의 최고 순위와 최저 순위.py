answer = [6, 6, 5, 4, 3, 2, 1]

def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    count = 0
    for num in lottos:
        if num in win_nums:
            count += 1
    return answer[count + zero_count], answer[count]