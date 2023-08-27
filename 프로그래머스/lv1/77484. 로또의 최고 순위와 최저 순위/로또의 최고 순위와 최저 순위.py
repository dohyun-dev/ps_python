answer = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

def solution(lottos, win_nums):
    win_nums = set(win_nums)
    zero_count = lottos.count(0)
    count = 0
    for num in lottos:
        if num in win_nums:
            count += 1
    return answer[count + zero_count], answer[count]