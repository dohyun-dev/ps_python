def calc_nums(num_list):
    global min_answer, max_answer
    result = sum(num_list)
    min_answer = min(min_answer, result)
    max_answer = max(max_answer, result)

def count(num):
    return len([1 for n in list(map(int, num)) if n != 0 and n % 2 == 1])

def solve(num, result=[]):
    result = result + [count(num)]
    if len(num) == 1:
        calc_nums(result)
        return
    elif len(num) == 2:
        calc_num = str(int(num[0]) + int(num[1]))
        solve(calc_num, result)
    else:
        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                calc_num = str(int(num[:i]) + int(num[i:j]) + int(num[j:]))
                solve(calc_num, result)
N = input()
min_answer, max_answer = float("inf"), 0
solve(N)
print(min_answer, max_answer)